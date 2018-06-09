import requests
import base64
import json
import time

chain_url = "https://apiplus-api-sandbox-testnet.factom.com/v1/chains"
headers = {
    "Content-Type": "application/json",
    "factom-provider-token": "D5Sf9ibJxKN4NSHRTpx3OTt5vwfpepIWnE5opJTGKVvBDiJ6"
}

def createChain():
    voting_station = input("Please enter an ID for the voting station you want to create:\n")

    b_unixtime = base64.b64encode(str(time.time()).encode('ascii')).decode('UTF-8')
    b_content = base64.b64encode(b"Contains vote counts for this voting station.").decode('UTF-8')
    b_exid = base64.b64encode(voting_station.encode('ascii')).decode('UTF-8')

    payload = {"external_ids":[b_exid, b_unixtime],"content":b_content}

    response = requests.post(chain_url, data=json.dumps(payload), headers = headers)
    print(response.text)

def updateChain(vote, voting_station):
    pass

def queryChain():
    chainID = input("please enter chainID:\n")
    chain_url_id = chain_url + "/"+chainID

    response = requests.get(chain_url_id, headers = headers)

    print(response.text)
