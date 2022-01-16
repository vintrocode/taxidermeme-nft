# make sure the withdrawal function only works for the deployer of the contract
# what's odd to me is that the transactions trying to withdraw to an unauthorized account don't fail...
# they just don't do anything. sketch if you don't actually dig in

import pytest
from brownie import Taxidermeme, accounts

@pytest.fixture
def taxidermeme():
    return Taxidermeme.deploy({'from': accounts[6]})

def test_withdrawal(taxidermeme):
    # mint a NFT from a new account, value should be stored in the contract
    taxidermeme.mint(accounts[5], "1.json", {'from': accounts[5], 'value': 20000000000000000})
    # check the balance of the contract, make sure the mints went as planned
    assert taxidermeme.balance() == 20000000000000000
    # try to withdraw the balance to one of the minting accounts
    taxidermeme.withdraw({'from': accounts[5]})
    # check that that account's balance didn't change from minting
    assert accounts[5].balance() == 99980000000000000000
    # try to withdraw to the deployment address, check that it worked
    taxidermeme.withdraw({'from': accounts[6]})
    assert accounts[6].balance() == 100020000000000000000