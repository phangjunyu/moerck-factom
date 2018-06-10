import chainFunctions as cf
import json

class FinalCount:
    def __init__(self):
        self.counter = {}
        self.votingStationList = ['5b856957cd2630858fa466093c5f8afa24ed640c2c7fa82bc64338a9d1c00afa']

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
