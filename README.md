# Taxidermemes NFT Repository

This project is based off a Vyper ERC721 [implementation](https://github.com/tserg/vyper-contracts/blob/main/contracts/ERC721.vy) and is tested/deployed using [brownie](https://eth-brownie.readthedocs.io/en/stable/index.html). The official contract is deployed [here](https://etherscan.io/address/0x37141f20895281d04f2a5b57dbaff4855daf9971). The collection features 150 unique Taxidermemes perfectly suited for mounting on your Twitter profile!

# How to Mint

Minting happens through writing to the contract on Etherscan. There is a max supply of 150, a limit of 2 mints per address, and the mint price is 0.02 ETH.

1. Follow [this link](https://etherscan.io/address/0x37141f20895281d04f2a5b57dbaff4855daf9971#writeContract) to the `Write Contract` section of Etherscan.

2. Find the button that says "Connect to Web3" and connect your wallet.

3. Click the `6. mint` function and you'll see 3 parameters: `payableAmount (ether)`, `_to (address)`, and `_tokenURI (string)`.
    `payableAmount (ether)` is the mint price, enter `0.02`.
    `_to (address)` is the address you want to send the NFT to.
    `_tokenURI (string)` is a string corresponding to the metadata file that points to the meme you want. It will simply be a `number.json` where `number` is any value from 1:150.

4. Once you're confident all the parameters are correct, click the `Write` button. This will pop up Metamask to confirm the transaction and mint your NFT.

5. **IMPORTANT:** Please go to [this google sheet](https://docs.google.com/spreadsheets/d/1VkxdxR7uSevSn2SuglfJxE3NuyAPXIFPNlBM-tUBIog/edit?usp=sharing) and mark which number you minted under the `is_taken` column, because transactions will revert if someone tries to mint the same NFT as you (aka write to the contract with the same `_tokenURI` param). Save your fellow degens gas and help them out by marking the sheet. Or help us build a front end to automate this. Either or :)

That's it, let us know how you like it by tweeting at us [@taxidermemes](https://twitter.com/taxidermemes)!

# Brownie

Clone this repository. Open up a brownie console and [add](https://eth-brownie.readthedocs.io/en/stable/api-network.html?highlight=accounts#localaccount) a deployment account to the [saved accounts](https://eth-brownie.readthedocs.io/en/stable/api-network.html?highlight=accounts#localaccount-methods) in brownie. 

To run tests, it's as easy as:
```
brownie test
```

To create metadata, make a `metadata/` folder at the root of the project directory and then run:
```
python scripts/create_metadata.py
```
Then upload those files to IPFS. Obtain the base URI from that upload an replace the value for `_baseURI` in `contracts/Taxidermeme.vy`.

To deploy, it's also simple:
```
brownie run scripts/deploy.py --network <network>
```