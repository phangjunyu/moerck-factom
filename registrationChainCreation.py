import requests
import base64
import json
import time

chain_url = "https://apiplus-api-sandbox-testnet.factom.com/v1/chains"
headers = {
    "Content-Type": "application/json",
    "factom-provider-token": "D5Sf9ibJxKN4NSHRTpx3OTt5vwfpepIWnE5opJTGKVvBDiJ6"
}

def createChain(chainID, description):

    b_unixtime = base64.b64encode(str(time.time()).encode('ascii')).decode('UTF-8')
    b_content = base64.b64encode(description).decode('UTF-8')
    b_exid = base64.b64encode(chainID.encode('ascii')).decode('UTF-8')

    payload = {"external_ids":[b_exid, b_unixtime],"content":b_content}

    response = requests.post(chain_url, data=json.dumps(payload), headers = headers)
    print(response.text)

def generateTokens(sizeOfToken, numberOfTokens):
    tokenList = []
    for i in range(numberOfTokens):

    return tokenList

def populateValidChain(tokenList):
    for token in tokenList:
        updateChain(token, 'List of Valid Tokens')


def updateChain(token, chainID):
    #jun yu currently working on it
    pass

def queryChain():
    chainID = input("please enter chainID:\n")
    chain_url_id = chain_url + "/"+chainID

    response = requests.get(chain_url_id, headers = headers)

    print(response.text)








createChain('List of Valid Tokens', b'Contains the list of all available valid tokens')
createChain('List of Used Tokens', b'Contains the list of all used tokens')