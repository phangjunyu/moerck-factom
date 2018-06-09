import registrationFunctions as cf
import time, secrets
class Vote:
    def __init__(self, choice, votingStationID, token):
        self.choice = choice
        self.votingstationID = votingstationID

class VoteManager:
    def __init__(self, votingStationID):
        self.votingStationID = votingStationID
    def receiveVote(choice, user):
        if validate(user):
            vote = Vote(choice, votingStationID)
            return vote
        else:
            print('Voter has already voted or has not been registered')
            return False

    def validate(user):
        return cf.checkTokens('va', user) and cf.checkVA(user)

    def submitVote(vote):
        zzTime = secrets.randbelow(10)
        time.sleep(zzTime)
        cf.updateChain(vote.choice ,vote.votingStationID, 'vote')
        cf.putVA(user)
