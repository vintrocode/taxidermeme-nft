import pytest
from brownie import Taxidermeme, accounts

@pytest.fixture
def taxidermeme():
    return Taxidermeme.deploy({'from': accounts[0]})

def test_excess_minting(taxidermeme):
    # the limit on minting should be 2. get to 2, and try 3. should fail
    for i in range(1, 3):
        taxidermeme.mint(accounts[1], "{}.json".format(i), {'from': accounts[1], 'value': 20000000000000000})
    
    try:
        taxidermeme.mint(accounts[1], "3.json", {'from': accounts[1], 'value': 20000000000000000})
    except:
        pass
        