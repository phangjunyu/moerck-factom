import registrationFunctions as rf
import time, secrets
from glossary import VA, RA
class Vote:
    def __init__(self, choice):
        self.choice = choice

class PollingBooth:
    def __init__(self, votingStationID):
        self.votingStationID = votingStationID

    def receiveVote(choice, userID):
        if validate(userID):
            vote = Vote(choice)
            return vote
        else:
            print('Voter has already voted or has not been registered')
            return False

    def validate(userID):
        return (not rf.checkTokens(VA, userID)) and rf.checkTokens(RA, userID)

    def submitVote(vote):
        zzTime = secrets.randbelow(10)
        time.sleep(zzTime)
        cf.updateChain({'vote' : vote.choice} ,vote.votingStationID)
        cf.putVA(user)

if __name__ = 'main':
    #we assume that we have created a voting station by now and have its chain ID
    #when a user enters we first check
    votingStationID = 'c4a852f7e5216f315093f7024b6e9f445cbce22e142de3b034b4def1834ff0bd'
    pollingbooth = PollingBooth(votingStationID)
    voterID = 'jcknwjkdn'

    #check if user already exist in the voter chain
    if checkUserExist(voterID):
        voterChainID = rf.getChainID(voterEX_ID)
    else:
        voterChainID = rf.createVoter(voterEX_ID)
    #put the RA token of the voter
    rf.putToken(RA, voterChainID)
    #once the RA token of the voter has been set, the voter is ready to vote
    choice = input('vote')
    vote = pollingbooth.receiveVote(choice, voterChainID)
    if vote is False:
        raise ValueError
    else:
        pollingbooth.submitVote(vote)
