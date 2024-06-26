from ape.api.accounts import AccountAPI
from ape.contracts import ContractInstance


def test_smoke(
    acct1: AccountAPI, acct2: AccountAPI, acct3: AccountAPI, weth_contract: ContractInstance
) -> None:
    assert acct1.balance > 0
    assert acct2.balance > 0
    assert acct3.balance > 0
    assert weth_contract.balance == 0
    assert weth_contract.totalSupply() == 0


def test_transfer(acct1: AccountAPI, acct2: AccountAPI, weth_contract: ContractInstance) -> None:
    weth_contract.deposit(value=100, sender=acct1)
    # tx_receipt = weth_contract.transfer(acct2, 35, sender=acct1)
    _ = weth_contract.transfer(acct2, 35, sender=acct1)

    assert weth_contract.balanceOf(acct1) == 65
    assert weth_contract.balanceOf(acct2) == 35
    assert weth_contract.totalSupply() == 100
