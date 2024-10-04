import json

from datetime import UTC, datetime
from decimal import Decimal

import pytz

from ape import Contract, networks
from dotenv import load_dotenv


load_dotenv()

# Define the Uniswap V2 Factory contract address
UNISWAP_V2_FACTORY_ADDRESS = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"

# Define the token addresses (e.g., WETH and USDC)
TOKEN0_ADDRESS = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"  # WETH
TOKEN1_ADDRESS = "0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"  # USDC


with open(".build/contract.json") as f:
    abi_pair = json.load(f)


rome_tz = pytz.timezone("Europe/Rome")


# NOTE: run `ape networks list` in terminal to see options
with networks.parse_network_choice("ethereum:mainnet-fork:hardhat") as hardhat_local_provider:
    print(f"Hardhat Provider connection status: {hardhat_local_provider.is_connected}")

    # hardhat_local_provider.unlock_account()
    # hardhat_local_provider.query_manager
    # hardhat_local_provider.local_project
    # hardhat_local_provider.config_manager
    # hardhat_local_provider.chain_manager
    # hardhat_local_provider.poll_blocks()
    hardhat_local_provider.set_timestamp(int(datetime.now().timestamp()))

    print(f"{hardhat_local_provider.name=}")
    # hardhat_local_provider.get_block('latest')=Block(num_transactions=177, hash=HexBytes('0x7107e48dbb8b75738475c0e14d12f7dcc29cfeb2aa791f00a7e5888ac7da248b'), number=20205559, parent_hash=HexBytes('0xa8c223102be2626cb97c26edef55aa9fdf9b13a5bec1c419124a6afa6f6212e6'), timestamp=1719763247,
    block = hardhat_local_provider.get_block("latest")
    print(f"{block.number=}")
    utc_time = datetime.fromtimestamp(block.timestamp, UTC)
    rome_time = utc_time.astimezone(rome_tz)

    print("Block timestamp (UTC):", utc_time)
    print("Block timestamp (Rome time):", rome_time)

    # contract_factory = Contract(address=UNISWAP_V2_FACTORY_ADDRESS)

    # pair_address = contract_factory.getPair(TOKEN0_ADDRESS, TOKEN1_ADDRESS)
    # if pair_address == "0x0000000000000000000000000000000000000000":
    #     print("Pair does not exist.")
    # else:
    #     print("Pair address:", pair_address)
    pair_address = "0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc"

    contract_pair = Contract(address=pair_address, abi=abi_pair)
    # contract_pair = Contract(address=pair_address)

    # token0 = contract_pair.token0()
    # token1 = contract_pair.token1()

    token0 = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
    token1 = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

    print(f"Token0 address: {token0}")
    print(f"Token1 address: {token1}")

    reserves = contract_pair.getReserves()
    reserve0_raw = reserves[0]
    reserve1_raw = reserves[1]

    print(f"Raw Reserve0 (WETH): {reserve0_raw}")
    print(f"Raw Reserve1 (USDC): {reserve1_raw}")

    if token0 == TOKEN1_ADDRESS and token1 == TOKEN0_ADDRESS:
        reserve0 = Decimal(reserve0_raw) / Decimal(10**6)  # USDC in USDC
        reserve1 = Decimal(reserve1_raw) / Decimal(10**18)  # WETH in ETH
    else:
        reserve0 = Decimal(reserve1_raw) / Decimal(10**6)  # USDC in USDC
        reserve1 = Decimal(reserve0_raw) / Decimal(10**18)  # WETH in ETH

    print(f"Reserve0 (WETH): {reserve0} ETH")
    print(f"Reserve1 (USDC): {reserve1} USDC")

    # Calculate the price of 1 WETH in USDC
    price = reserve1 / reserve0
    print(f"The price of 1 WETH in USDC is: {price} USDC")

    # Check the total supply of the liquidity pool tokens
    # total_supply = contract_pair.totalSupply()
    # print(f"Total supply of LP tokens: {total_supply}")

    # Check the balance of each token in the pair contract
    # balance_token0 = contract_pair.balanceOf(token0)
    # balance_token1 = contract_pair.balanceOf(token1)

    # print(f"Balance of Token0 (WETH): {balance_token0}")
    # print(f"Balance of Token1 (USDC): {balance_token1}")
