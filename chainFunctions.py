import requests
import base64
import json
import time

chain_url = "https://apiplus-api-sandbox-testnet.factom.com/v1/chains"
headers = {
    "Content-Type": "application/json",
    "factom-provider-token": "D5Sf9ibJxKN4NSHRTpx3OTt5vwfpepIWnE5opJTGKVvBDiJ6"
}


def main():
    print ("In Main")

def createVoteChain(voting_station_id):

    b_unixtime = base64.b64encode(str(time.time()).encode('ascii')).decode('UTF-8')
    b_content = base64.b64encode(b"Contains vote counts for this voting station.").decode('UTF-8')
    b_exid = base64.b64encode(voting_station_id.encode('ascii')).decode('UTF-8')
    payload = {"external_ids":[b_exid, b_unixtime],"content":b_content}

    response = requests.post(chain_url, data=json.dumps(payload), headers = headers)
    print(json.dumps(response.json(), sort_keys=True, indent=4))

def updateChain(vote, external_ids):
    b_vote = base64.b64encode(vote.encode('ascii')).decode('UTF-8')

    payload = {"external_ids":external_ids, "content": b_vote}
    response = requests.request("POST", chain_url, data=json.dumps(payload), headers = headers)

    print(response.text)

def queryChain(chainID):

    chain_url_id = chain_url + "/"+chainID

    response = requests.get(chain_url_id, headers = headers)

    print(json.dumps(response.json(), sort_keys=True, indent=4))
