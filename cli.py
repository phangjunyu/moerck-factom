#Creates an input interface for user to enter options through command line
import chainFunctions as cf

def createVotingStation():
    voting_station_id = input("Please enter an ID for the voting station you want to create:\n")
    status = cf.createVoteChain(voting_station_id)
    print(json.dumps(status, sort_keys=True, indent=4))

def update():
    chainID = input("Please enter chainID:\n")
    external_ids = cf.getChainExternalIDs(chainID)
    contentType = input("Please enter entryType:\n")
    entry = input("Please enter entry:\n")
    status = cf.updateChain(entry, external_ids, contentType)
    print(status)

def query():
    chainID = input("please enter chainID:\n")
    query = cf.queryChain(chainID)
    print(query)

def getEntries():
    chainID = input("please enter chainID:\n")
    entries = cf.getEntries(chainID)
    print(entries)
