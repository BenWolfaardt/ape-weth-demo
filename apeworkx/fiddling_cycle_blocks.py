import time

from ape import networks
from dotenv import load_dotenv


load_dotenv()


def configure_and_fork_at_block_number(block_number: int) -> None:
    config = {
        "host": "127.0.0.1:8556",
        "upstream_provider": "alchemy",
        "block_number": str(block_number),
        "enable_hardhat_deployments": False,
    }

    # config = {"fork_block_number": block_number}

    with networks.parse_network_choice("ethereum:mainnet:alchemy") as alchemy_provider:
        print(
            f"{alchemy_provider.name.capitalize()} Provider connection status: {alchemy_provider.is_connected}"
        )

        block = alchemy_provider.get_block("latest")
        print(f"Latest retrieved block height is: {block.number}")

        with networks.fork(
            provider_name="hardhat", provider_settings=config, block_number=block_number
        ) as provider_context:
            # Current config
            print(provider_context.config.model_dump_json)

            block = provider_context.get_block("latest")
            print(f"Forked network block number: {block.number}")

            blocks = range(20892999, 20893000)
            for block_number in blocks:
                block = provider_context.get_block(str(block_number))
                print(f"Getting block data for block height: {block.number}")
                time.sleep(0.3)

            # Above this line works

            print("Updating settings")
            # NOTE: results in a new connection to hardhat
            provider_context.update_settings(config)

            # Supossed new updated settings
            print(provider_context.config.model_dump)
            block = provider_context.get_block("latest")
            print(f"Forked network block number: {block.number}")


if __name__ == "__main__":
    block_number = 2000000
    configure_and_fork_at_block_number(block_number)

    # class HardhatForkConfig(BaseModel):
    #     host: str
    #     upstream_provider: str
    #     block_number: int
    #     enable_hardhat_deployments: bool

    # config = {
    #     'evm_version': None,
    #     'host': None,
    #     'manage_process': True,
    #     'bin_path': None,
    #     'request_timeout': 30,
    #     'fork_request_timeout': 300,
    #     'process_attempts': 5,
    #     'hardhat_config_file': None,
    #     'fork': {
    #         'ethereum': {
    #             'mainnet': {
    #                 'host': '127.0.0.1:8555',
    #                 'upstream_provider': 'alchemy',
    #                 'block_number': block_number,
    #                 'enable_hardhat_deployments': 'true'
    #             }
    #         }
    #     }
    # }

    # config = {
    #     'evm_version': None,
    #     'host': None,
    #     'manage_process': True,
    #     'bin_path': None,
    #     'request_timeout': 30,
    #     'fork_request_timeout': 300,
    #     'process_attempts': 5,
    #     'hardhat_config_file': None,
    #     'fork': {
    #         'ethereum': {
    #             'mainnet': HardhatForkConfig(
    #                 host='127.0.0.1:8555',
    #                 upstream_provider='alchemy',
    #                 block_number=block_number,
    #                 enable_hardhat_deployments=False
    #             )
    #         }
    #     }
    # }