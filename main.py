import chainFunctions as cf

menu ="""select your choice:
    0) Create a chain
    1) Update a chain
    2) Query a chain
    """

choice = input(menu)

def createVote():
    voting_station_id = input("Please enter an ID for the voting station you want to create:\n")
    cf.createVoteChain(voting_station_id)

def update():
    cf.updateChain(vote, external_ids)

def query():
    chainID = input("please enter chainID:\n")
    cf.queryChain(chainID)

options = {
  '0': createVote(),
  '1': update(),
  '2': query()
}

options[choice]()
