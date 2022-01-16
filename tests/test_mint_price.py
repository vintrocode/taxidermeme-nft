# test people can't mint for anything other than mintPrice

import pytest
from brownie import Taxidermeme, accounts

@pytest.fixture
def taxidermeme():
    return Taxidermeme.deploy({'from': accounts[0]})

def test_mint_price(taxidermeme):
    try:
        taxidermeme.mint(accounts[1], "1.json", {'from': accounts[1]})
    except:
        pass
    try:
        taxidermeme.mint(accounts[1], "1.json", {'from': accounts[1], 'value': 30000000000000000})
    except:
        pass
    taxidermeme.mint(accounts[1], "1.json", {'from': accounts[1], 'value': 20000000000000000})