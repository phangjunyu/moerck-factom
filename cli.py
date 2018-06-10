#Creates an input interface for user to enter options through command line
import chainFunctions as cf
import registrationFunctions as rf
import json
import FinalCount as fc
import base64

def createVotingStation():
    voting_station_id = input("Please enter an ID for the voting station you want to create:\n")
    first = input("Enter candidate one")
    second = input("Enter candidate two")
    candidates = [first, second]
    status = cf.createVoteChain(voting_station_id, candidates)
    print(json.dumps(status, sort_keys=True, indent=4))

def update():
    chainID = input("Please enter chainID:\n")
    entry = input("Please enter entry:\n")
    status = cf.updateChain(entry, chainID)
    print(status)

def query():
    chainID = input("please enter chainID:\n")
    query = cf.queryChain(chainID)
    print(query)

def getEntries():
    chainID = input("please enter chainID:\n")
    entries = cf.getEntries(chainID)
    print(entries)

def createVoterChain():
    name = input("Please enter your name:\n")
    uid = input("Please enter your uid:\n")
    status = rf.createVoter(name, uid)
    print(status)

def putToken():
    chainID = input("Please enter chainID:\n")
    type = input("Please enter type (VA or RA):\n")
    status = rf.putToken(type, chainID)
    print(status)

def checkToken():
    chainID= input("Please enter chainID:\n")
    type = input("Please enter type (VA or RA):\n")
    status = rf.checkTokens(type, chainID)
    print(status)

def checkVoter():
    name = input("Please enter name:\n")
    uid = input("Please enter uid:\n")
    status = rf.checkVoter(name, uid)
    voter_ = status['items']
    if len(voter_) == 0:
        print("voter does not exist")
    else:
        print("Voter's chain_id is:", voter_[0]['chain_id'])

def getFinalCount():
    final_count = fc.FinalCount()
    print (final_count.countFinalTally())

def getCandidates(chainID):
    # chainID = input("please enter chainID:\n")
    first_entry = cf.queryChain(chainID)['links']['first']
    result = cf.getEntry(first_entry)
    content = base64.b64decode(result['content']).decode('UTF-8')
    content = json.loads(content)
    candidates = content['candidates']
    for candidate in candidates:
        print (candidate)
    return candidates

    # print(json.dumps(result, sort_keys=True, indent=4))
