import pytest

from ape.api.accounts import AccountAPI
from ape.contracts import ContractContainer, ContractInstance
from ape.managers.accounts import TestAccountAPI
from ape.managers.project import ProjectManager


@pytest.fixture
def acct1(accounts: TestAccountAPI) -> AccountAPI:
    return accounts[0]


@pytest.fixture
def acct2(accounts: TestAccountAPI) -> AccountAPI:
    return accounts[1]


@pytest.fixture
def acct3(accounts: TestAccountAPI) -> AccountAPI:
    return accounts[2]


@pytest.fixture
def weth_contract(acct1: AccountAPI, project: ProjectManager) -> ContractInstance:
    weth9: ContractContainer = project.WETH9
    return acct1.deploy(weth9)
