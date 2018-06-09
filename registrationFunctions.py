import chainFunctions as cf
import base64
import json
import requests

chain_url = "https://apiplus-api-sandbox-testnet.factom.com/v1/chains"
headers = {
    "Content-Type": "application/json",
    "factom-provider-token": "D5Sf9ibJxKN4NSHRTpx3OTt5vwfpepIWnE5opJTGKVvBDiJ6"
}

def createVoter(name, uid):
    b_name = base64.b64encode(name.encode('ascii')).decode('UTF-8')
    b_info = base64.b64encode(b"This is a voter").decode('UTF-8')
    b_uid = base64.b64encode(uid.encode('ascii')).decode('UTF-8')
    payload = {"external_ids":[b_name, b_uid],"content":b_info}

    response = requests.post(chain_url, data=json.dumps(payload), headers = headers)
    return response.json()

def checkTokens(type, voterID):
    voter_url = chain_url + "/" + voterID

    response = requests.get(voter_url, headers = headers)
    response = response.json()

    # print(json.dumps(response, sort_keys=True, indent=4))

    links = response['links']
    last_entry = links['last']
    response_last = requests.get(last_entry, headers = headers)

    print(json.dumps(response_last.json(), sort_keys=True, indent=4))
    content = base64.b64decode(response_last.json()['content']).decode('UTF-8')
    print (content)

    if content == "This is a voter":
        print ("No " + type + " recorded")
        return False
    else:
        print (type + " is " + content[type])
        return content[type]
