import chainFunctions as cf

chain_url = "https://apiplus-api-sandbox-testnet.factom.com/v1/chains"
headers = {
    "Content-Type": "application/json",
    "factom-provider-token": "D5Sf9ibJxKN4NSHRTpx3OTt5vwfpepIWnE5opJTGKVvBDiJ6"
}

def createVoter(name, uid):
    b_name = base64.b64encode(name).encode('ascii')).decode('UTF-8')
    b_info = base64.b64encode("This is a voter").decode('UTF-8')
    b_uid = base64.b64encode(uid).encode('ascii')).decode('UTF-8')
    payload = {"external_ids":[b_name, b_uid],"content":b_content}

    response = requests.post(chain_url, data=json.dumps(payload), headers = headers)
    return response.json()
