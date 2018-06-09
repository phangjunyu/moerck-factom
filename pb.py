import chainFunctions as cf
import time, secrets
class Vote:
    def __init__(self, choice, votingStationID, token):
        self.choice = choice
        self.votingstationID = votingstationID

class VoteManager:

    def receiveVote(choice, votingStationID, user):
        if validate(user):
            vote = Vote(choice, votingStationID)
            return vote
        else:
            print('Voter has already voted or has not been registered')
            return False

    def validate(user):
        return checkRA(user) and checkVA(user)

    def submitVote(vote):
        zzTime = secrets.randbelow(10)
        time.sleep(zzTime)
        cf.updateChain(vote.choice ,vote.votingStationID, 'vote')
