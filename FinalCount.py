import chainFunctions as cf
import json

class FinalCount:
    def __init__(self):
        self.counter = {}
        self.votingStationList = ['c4a852f7e5216f315093f7024b6e9f445cbce22e142de3b034b4def1834ff0bd']

    def addVotingStation(self, votingStationID):
        self.votingStationList.append(votingStationID)

    def countFinalTally(self):
        for station in self.votingStationList:
            entries = cf.getEntries(station)
            listJson = entries['content']
            for jsonString in listJson:
                try:
                    vote = self.formatJson(jsonString)
                    if vote['vote'] in self.counter:
                        self.counter[vote['vote']]+= 1
                    else:
                        self.counter[vote['vote']] = 1
                except:
                    continue
        return self.counter

    def formatJson(self,jsonString):
        jsonDictionary = json.loads(jsonString)
        return jsonDictionary

# fn = FinalCount()
# print(fn.countFinalTally())
