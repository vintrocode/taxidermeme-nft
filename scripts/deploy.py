from brownie import Taxidermeme, accounts


def main():
    acct = accounts.load('taxidermeme')
    print(acct)
    Taxidermeme.deploy({"from": acct})