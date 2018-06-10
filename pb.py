import registrationFunctions as rf
import chainFunctions as cf
import time, secrets
from glossary import VA, RA
import FinalCount
class Vote:
    def __init__(self, choice):
        self.choice = choice

class PollingBooth:
    def __init__(self, votingStationID):
        self.votingStationID = votingStationID

    def receiveVote(self, choice, userID):
        if self.validate(userID):
            vote = Vote(choice)
            return vote
        else:
            print('Voter has already voted or has not been registered')
            return False

    def validate(self, userID):
        return (not rf.checkTokens(VA, userID)) and rf.checkTokens(RA, userID)

    def submitVote(self, vote, userID):
        zzTime = secrets.randbelow(10)
        #time.sleep(zzTime)
        cf.updateChain({
                        'vote' : vote.choice,
                        'UnixTimeStamp' : str(time.time())
                        } , self.votingStationID)
        rf.putToken(VA, userID)
        print('voted for', vote.choice)

def checkVoter(name, uid):
    status = rf.checkVoter(name, uid)
    voter_ = status['items']
    if len(voter_) == 0:
        return False
    else:
        return voter_[0]['chain_id']

if __name__ == '__main__':
    #we assume that we have created a voting station by now and have its chain ID
    #when a user enters we first check

    votingStationID = 'c4a852f7e5216f315093f7024b6e9f445cbce22e142de3b034b4def1834ff0bd'
    pollingbooth = PollingBooth(votingStationID)
    voterName = 'JY'
    voterID = 'jcknwjkdn'

    #check if user already exist in the voter chain
    voterChainID = checkVoter(voterName, voterID)
    if not voterChainID:
        status = rf.createVoter(voterName, voterID)
        voterChainID = status['chain_id']

    #put the RA token of the voter
    rf.putToken(RA, voterChainID)
    #once the RA token of the voter has been set, the voter is ready to vote
    choice = input('vote')
    vote = pollingbooth.receiveVote(choice, voterChainID)
    if vote is False:
        raise ValueError
    else:
        pollingbooth.submitVote(vote, voterChainID)

    fn = FinalCount.FinalCount()
    results = fn.countFinalTally()
    print (results)
