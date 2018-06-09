import cli

menu ="""select your choice:
    0) Create a chain
    1) Update a chain
    2) Query a chain
    3) Get all entries of a chain
    """

choice = input(menu)

options = {
  '0': cli.createVotingStation,
  '1': cli.update,
  '2': cli.query,
  '3': cli.getEntries
}

options[choice]()
