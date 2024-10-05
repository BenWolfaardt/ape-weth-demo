import time

from ape import networks
from dotenv import load_dotenv


load_dotenv()

block_number = 20892999

ecosystem_name = "ethereum"
network_name = "mainnet"
provider_name = "alchemy"
# network_choice = f"{ecosystem_name}:{network_name}:{provider_name}"
network_choice = f"{ecosystem_name}:{network_name}"

provider_settings = {
    "host": "127.0.0.1:8555",
    # "upstream_provider": "alchemy",  # NOTE: note sure we can set it here
    # "block_number": str(block_number),  # NOTE: the provider will get the latest block it can
    "enable_hardhat_deployments": False,
    # "fork_block_number": str(block_number)  # NOTE: the provider will get the latest block it can
}

with networks.parse_network_choice(
    network_choice=network_choice, provider_settings=provider_settings
) as provider:
    print(f"{provider.name.capitalize()} Provider connection status: {provider.is_connected}")

    block = provider.get_block("latest")
    print(f"Latest retrieved block height is: {block.number}")

    print(provider.settings)

    fork_provider_name = "hardhat"
    fork_provider_settings = {
        "host": "127.0.0.1:8556",
        # "upstream_provider": "alchemy",
        # "block_number": "20892999",
        "enable_hardhat_deployments": True,
    }

    with networks.fork(
        provider_name=fork_provider_name,
        provider_settings=fork_provider_settings,
        # block_number=block_number  # NOTE: .fork should automatically pick the latest block
        #   https://discord.com/channels/922917176040640612/1004472541898870904/1258048955443576912
    ) as provider_context:
        # Current config
        # print(provider_context.config.model_dump_json)
        print(provider_context.settings)

        block = provider_context.get_block("latest")
        # block = provider_context.get_block(fork_provider_settings["block_number"])
        print(f"Forked network block number: {block.number}")

        blocks = range(20892999, 20892999)
        for block_number in blocks:
            block = provider_context.get_block(str(block_number))
            print(f"Getting block data for block height: {block.number}")
            time.sleep(0.3)

        # Above this line works
        # update_fork_config = {
        #     "host": "127.0.0.1:8557",
        #     # "upstream_provider": "alchemy",
        #     "block_number": str(block_number),
        #     "enable_hardhat_deployments": True,
        # }
        update_fork_config = {
            "fork": {"ethereum": {"mainnet": {"upstream_provider": "alchemy", "block_number": "20891999"}}}
        }

        print("Updating settings")
        # NOTE: results in a new connection to hardhat
        provider_context.update_settings(update_fork_config)

        print(provider_context.settings)

        # Supossed new updated settings
        # print(provider_context.config.model_dump)
        block = provider_context.get_block("latest")
        print(f"Forked network block number: {block.number}")
