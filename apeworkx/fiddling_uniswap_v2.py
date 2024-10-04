from decimal import Decimal

from ape import Contract, networks
from dotenv import load_dotenv


load_dotenv()

# Define the Uniswap V2 Factory contract address
UNISWAP_V2_FACTORY_ADDRESS = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"

# Define the token addresses (e.g., WETH and USDC)
TOKEN0_ADDRESS = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"  # WETH
TOKEN1_ADDRESS = "0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"  # USDC


with networks.parse_network_choice("ethereum:mainnet:alchemy") as alchemy_provider:
    print(f"Alchemy Provider connection status: {alchemy_provider.is_connected}")

    contract_factory = Contract(address=UNISWAP_V2_FACTORY_ADDRESS)

    pair_address = contract_factory.getPair(TOKEN0_ADDRESS, TOKEN1_ADDRESS)
    if pair_address == "0x0000000000000000000000000000000000000000":
        print("Pair does not exist.")

    contract_pair = Contract(address=pair_address)

    token0 = contract_pair.token0()
    token1 = contract_pair.token1()

    print(f"Token0 address: {token0}")
    print(f"Token1 address: {token1}")

    reserves = contract_pair.getReserves()
    reserve0_raw = reserves[0]
    reserve1_raw = reserves[1]

    print(f"Raw Reserve0 (WETH): {reserve0_raw}")
    print(f"Raw Reserve1 (USDC): {reserve1_raw}")

    # Adjusting reserve assignments based on token addresses
    if token0.lower() == TOKEN0_ADDRESS.lower():  # WETH is token0
        reserve0 = Decimal(reserve0_raw) / Decimal(10**18)  # WETH in ETH
        reserve1 = Decimal(reserve1_raw) / Decimal(10**6)  # USDC in USDC
    else:  # USDC is token0
        reserve0 = Decimal(reserve1_raw) / Decimal(10**6)  # USDC in USDC
        reserve1 = Decimal(reserve0_raw) / Decimal(10**18)  # WETH in ETH

    print(f"Reserve0 (WETH): {reserve0} ETH")
    print(f"Reserve1 (USDC): {reserve1} USDC")

    # Calculate the price of 1 WETH in USDC
    if reserve0 > 0:
        price = reserve1 / reserve0 * 10**24  # TODO: figure out why this constant?
        print(f"The price of 1 WETH in USDC is: {price} USDC")
    else:
        print("Reserve0 is zero, unable to calculate price.")

    # Check the total supply of the liquidity pool tokens
    total_supply = contract_pair.totalSupply()
    print(f"Total supply of LP tokens: {total_supply}")

    # Check the balance of each token in the pair contract
    balance_token0 = contract_pair.balanceOf(token0)
    balance_token1 = contract_pair.balanceOf(token1)

    print(f"Balance of Token0 (WETH): {balance_token0}")
    print(f"Balance of Token1 (USDC): {balance_token1}")
