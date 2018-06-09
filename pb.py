import registrationChainCreation as rcc
class Vote:
    def __init__(self, choice, votingStation, token):
        self.choice = choice
        self.votingstation = votingstation
        self.token = token

class VoteManager:

    def receiveVote(choice, votingStation, token):

        #check if token is valid
        isValid = Registration.validateToken(token)
        if isValid:
            vote = Vote(choice, votingStation, token)
            return vote
        else:
            print('Voter has already voted')
            return False


class Registration:

    def validateToken(token):
        tokenList = getTokenList()
        if token in tokenList:
            self.updateRegistrationChain(token)
            return True
        else:
            return False

    def updateRegistrationChain(token):
        #remove the token from the registration factom chain
        self.updateChain("List Of Used Tokens")

    def getTokenList():
        #get the token list from the registration chain
        valid  = rcc.queryChain('List of Valid Tokens')
        used = rcc.queryChain('List of Used Tokens')

        available = valid - used
        return available
