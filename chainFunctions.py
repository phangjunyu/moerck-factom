import requests
import base64
import json
import time

chain_url = "https://apiplus-api-sandbox-testnet.factom.com/v1/chains"
headers = {
    "Content-Type": "application/json",
    "factom-provider-token": "D5Sf9ibJxKN4NSHRTpx3OTt5vwfpepIWnE5opJTGKVvBDiJ6"
}

def createVoteChain(voting_station_id):

    b_unixtime = base64.b64encode(str(time.time()).encode('ascii')).decode('UTF-8')
    b_content = base64.b64encode(b"Contains vote counts for this voting station.").decode('UTF-8')
    b_exid = base64.b64encode(voting_station_id.encode('ascii')).decode('UTF-8')
    payload = {"external_ids":[b_exid, b_unixtime],"content":b_content}

    response = requests.post(chain_url, data=json.dumps(payload), headers = headers)
    return response.json()

def updateChain(entry, chainID, contentType):
    external_ids = getChainExternalIDs(chainID)
    content = {
        contentType: entry
    }
    b_content = base64.b64encode(json.dumps(content).encode('ascii')).decode('UTF-8')
    payload = {"external_ids":external_ids, "content": b_content}
    response = requests.request("POST", chain_url, data=json.dumps(payload), headers = headers)

    return response.text

#intermediate function for updateChain
def getChainExternalIDs(chainID):
    chain_url_id = chain_url + "/"+chainID

    response = requests.get(chain_url_id, headers = headers)
    external_ids = response.json()["external_ids"]
    return external_ids

#returns meta data of chain for reference purposes
def queryChain(chainID):
    chain_url_id = chain_url + "/"+chainID
    response = requests.get(chain_url_id, headers = headers)
    return response.json()

def getEntries(chainID):
    chain_url_id = chain_url + "/" + chainID + "/entries"

    response = requests.get(chain_url_id, headers = headers)
    response = response.json()

    entries = []

    #TODO: Remember to take out the first entry since it is the description
    for item in response['items']:
        entry_url = item['links']['entry']
        response_entry = requests.get(entry_url, headers = headers)
        content = base64.b64decode(response_entry.json()['content']).decode('UTF-8')
        entries.append(content)

    json_entries = {
        "content": entries
    }
    return json_entries
