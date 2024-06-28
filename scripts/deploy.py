import click

from ape import (
    accounts,  # "accounts" is the AccountManager singleton
    project,  # "accounts" is the ProjectManager singleton
)
from ape.api import EcosystemAPI
from ape.api.networks import NetworkAPI
from ape.api.providers import ProviderAPI
from ape.cli import (
    ApeCliContextObject,
    ConnectedProviderCommand,
    ape_cli_context,
    network_option,
)
from ape.exceptions import ProviderNotConnectedError


@click.command(cls=ConnectedProviderCommand)
@ape_cli_context()
@network_option()
def cli(
    cli_ctx: ApeCliContextObject, provider: ProviderAPI, ecosystem: EcosystemAPI, network: NetworkAPI
) -> None:
    cli_ctx.logger.debug(cli_ctx)  # TODO: leaks API Key
    cli_ctx.logger.debug(provider)
    cli_ctx.logger.debug(ecosystem)
    cli_ctx.logger.debug(network)

    try:
        if not provider.is_connected:
            raise ProviderNotConnectedError("Not connected to a network provider.")
    except Exception as e:
        raise ProviderNotConnectedError("Provider does not have 'is_connected' attribute.") from e

    network_name = network.name
    if network_name == "local" or network_name.endswith("-fork"):
        account = cli_ctx.account_manager.test_accounts[0]
    else:
        account = accounts.load("test")

    try:
        receipt = account.deploy(project.WETH9, gas_limit=2000000)  # Adjust gas_limit as needed
        cli_ctx.logger.info(f"Deployment successful. Transaction hash: {receipt.txn_hash}")
    except Exception as e:
        cli_ctx.logger.info(f"Deployment failed: {str(e)}")
