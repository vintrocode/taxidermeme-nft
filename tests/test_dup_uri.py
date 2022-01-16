# test that you can't mint the same _tokenURI
import pytest
from brownie import Taxidermeme, accounts

@pytest.fixture
def taxidermeme():
    return Taxidermeme.deploy({'from': accounts[0]})

def test_mint_dup(taxidermeme):
    # give account 1 the 1.json 
    taxidermeme.mint(accounts[1], "1.json", {'from': accounts[1], 'value': 20000000000000000})
    # give account 2 the 1.json, we expect a revert
    try:
        taxidermeme.mint(accounts[2], "1.json", {'from': accounts[2], 'value': 20000000000000000})
    except:
        print("Successfully reverted a tx trying to mint an already taken json")


