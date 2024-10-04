from ape import networks
from dotenv import load_dotenv


load_dotenv()


with networks.parse_network_choice("ethereum:sepolia:alchemy") as alchemy_provider:
    print(f"Alchemy Provider connection status: {alchemy_provider.is_connected}")

    print(f"{alchemy_provider.is_connected=}")
    print(f"{alchemy_provider.connection_str=}")  # TODO: leaks API Key
    print(f"{alchemy_provider.connection_id=}")
    print(f"{alchemy_provider.chain_id=}")
    print(f"{alchemy_provider.get_balance('0x2B6eD29A95753C3Ad948348e3e7b1A251080Ffb9')=}")
    print(f"{alchemy_provider.get_balance('0xe3f7A408a64E147e120f79Daa2973D890Cd9d830')=}")
    print(
        f"{alchemy_provider.get_nonce('0xe3f7A408a64E147e120f79Daa2973D890Cd9d830')=}"
    )  # number of times an account has transacted
    print(f"{alchemy_provider.gas_price=}")
    print(f"{alchemy_provider.max_gas=}")
    print(f"{alchemy_provider.config=}")
    print(f"{alchemy_provider.priority_fee=}")
    print(f"{alchemy_provider.base_fee=}")
    # print(alchemy_provider.get_block(6207349))
    receipt = alchemy_provider.get_receipt(
        "0xd57c1e4f6dee77594e9941534367136df7137d5a140d0c94bb42f429acaae821"
    )
    print(f"{receipt.block_number=}")
    print(f"{receipt.contract_address=}")
    print(f"{receipt.model_dump=}")
    print(f"{receipt.gas_used=}")
    print(f"{receipt.model_dump_json=}")
    print(f"{receipt.logs=}")
    print(f"{receipt.model_fields=}")
    print(f"{receipt.status=}")
    print(f"{receipt.transaction=}")
    print(f"{receipt.trace=}")
    print(f"{receipt.show_gas_report=}")
    # WARNING: Performing this action is likely to be very slow and may use 2000 or more RPC calls. Consider installing an alternative data query provider plugin.
    # transactions = alchemy_provider.get_transactions_by_account_nonce("0xe3f7A408a64E147e120f79Daa2973D890Cd9d830", 0, 100)  # account history for the given account
    # for tx in transactions:
    #     print(f"{tx=}")
    print(
        f"{alchemy_provider.get_transaction_trace('0xccaeda6f95976cac6e05e169a649e48c060bba25e8f55bbd25a3ce4c4f187970')=}"
    )
    # print(f"{alchemy_provider.get_contract_logs()=}")
    print(f"{alchemy_provider.supports_tracing=}")
