import chainFunctions as cf
import base64
import json
import requests
from glossary import VA, RA

chain_url = "https://apiplus-api-sandbox-testnet.factom.com/v1/chains"
headers = {
    "Content-Type": "application/json",
    "factom-provider-token": "D5Sf9ibJxKN4NSHRTpx3OTt5vwfpepIWnE5opJTGKVvBDiJ6"
}

def checkVoter(name, uid):
    chain_search_url = "https://apiplus-api-sandbox-testnet.factom.com/v1/chains/search"
    b_name = base64.b64encode(name.encode('ascii')).decode('UTF-8')
    b_uid = base64.b64encode(uid.encode('ascii')).decode('UTF-8')
    payload = {"external_ids":[b_name, b_uid]}
    response = requests.post(chain_search_url, data=json.dumps(payload), headers = headers)
    return response.json()

def createVoter(name, uid):
    b_name = base64.b64encode(name.encode('ascii')).decode('UTF-8')
    b_info = base64.b64encode(b"This is a voter").decode('UTF-8')
    b_uid = base64.b64encode(uid.encode('ascii')).decode('UTF-8')
    payload = {"external_ids":[b_name, b_uid],"content":b_info}

    response = requests.post(chain_url, data=json.dumps(payload), headers = headers)
    return response.json()

def putToken(type, chainID):
    ra_ = checkTokens(RA, chainID)
    va_ = checkTokens(VA, chainID)
    if type == RA and not ra_ and not va_:
        content = {
            RA: True,
            VA: va_
        }
    elif type == "VA" and not va_ and ra_:
        content = {
            RA: ra_,
            VA: True
        }
    else:
        return "Error, you are not allowed to submit a vote."
    return cf.updateChain(content, chainID)

def checkTokens(type, voterID):
    voter_url = chain_url + "/" + voterID

    response = requests.get(voter_url, headers = headers)
    response = response.json()

    # print(json.dumps(response, sort_keys=True, indent=4))

    links = response['links']
    last_entry = links['last']
    response_last = requests.get(last_entry, headers = headers)

    # print(json.dumps(response_last.json(), sort_keys=True, indent=4))
    content = base64.b64decode(response_last.json()['content']).decode('UTF-8')
    if content == "This is a voter":
        # print ("No " + type + " recorded")
        return False
    elif isinstance(content, str):
        content = json.loads(content)
        return content[type]
