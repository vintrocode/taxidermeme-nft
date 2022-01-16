# generate metadata for each image

import json

IMAGE_BASE_URL = "https://gateway.pinata.cloud/ipfs/QmVgddjNP3LH3YSPcBRqC9euQxcLKtnw7pRpXhQezzEK8f"
PROJECT_NAME = "Taxidermemes"
MAX_SUPPLY = 150  # there are 150 files and they are named 1.jpg -- 150.jpg

def main():
    # loop through the 150 files and make metadata jsons
    for i in range(MAX_SUPPLY):
        tokenId = i + 1    # i starts at 0, increment to 1
        name = "Taxidermeme " + str(i + 1)
        image = IMAGE_BASE_URL + "/" + str(i + 1) + ".jpg"
        token = {
            "image": image,
            "tokenId": tokenId,
            "name": name
        }

        with open("./metadata/" + str(tokenId) + ".json", 'w') as outfile:
            json.dump(token, outfile, indent=4)

if __name__ == "__main__":
    main()