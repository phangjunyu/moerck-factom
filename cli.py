#Creates an input interface for user to enter options through command line
import chainFunctions as cf
import registrationFunctions as rf

def createVotingStation():
    voting_station_id = input("Please enter an ID for the voting station you want to create:\n")
    status = cf.createVoteChain(voting_station_id)
    print(json.dumps(status, sort_keys=True, indent=4))

def update():
    chainID = input("Please enter chainID:\n")
    contentType = input("Please enter entryType:\n")
    entry = input("Please enter entry:\n")
    status = cf.updateChain(entry, chainID, contentType)
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

def putRA():
    chainID = input("Please enter chainID:\n")
    status = rf.putRA(chainID)
    print(status)

def checkToken():
    chainID= input("Please enter chainID:\n")
    type = input("Please enter type:\n")
    rf.checkTokens(type, chainID)
