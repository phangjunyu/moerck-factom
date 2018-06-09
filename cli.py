#Creates an input interface for user to enter options through command line
import chainFunctions as cf

def createVote():
    voting_station_id = input("Please enter an ID for the voting station you want to create:\n")
    cf.createVoteChain(voting_station_id)

def update():
    chainID = input("Please enter chainID:\n")
    external_ids = cf.getChainExternalIDs(chainID)
    vote = input("Please enter vote:\n")
    cf.updateChain(vote, external_ids)

def query():
    chainID = input("please enter chainID:\n")
    cf.queryChain(chainID)
