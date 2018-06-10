import chainFunctions as cf
import json

class FinalCount:
    def __init__(self):
        self.counter = {"red party": 0, "blue party": 0}
        self.votingStationList = []

    def addVotingStation(votingStationID):
        self.votingStationList.append(votingStationID)

    def countFinalTally():
        for station in votingStationList:
            stationVotingList = formatJson(cf.getEntries(station))
            for vote in stationVotingList:
                self.counter[vote['vote']]+= 1
        return self.counter

    def formatJson(jsonString):
        jsonDictionary = json.loads(jsonString)
        return jsonDictionary['content']
