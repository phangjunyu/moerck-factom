import cli

menu ="""select your choice:
    0) Registration Booth
    1) Voting Booth
    """

choice = input(menu)

if str(choice) == '1':
    menu ="""select your choice:
        0) Create a Voting Station
        1) Update a chain
        2) Query a chain
        3) Get all entries of a chain
        4) Show final count
        """

    choice = str(input(menu))

    options = {
      '0': cli.createVotingStation,
      '1': cli.update,
      '2': cli.query,
      '3': cli.getEntries,
      '4': cli.getFinalCount
    }

    options[choice]()
else:
    menu ="""select your choice:
        0) Register
        1) Check Tokens
        2) Put a Token
        3) Check Voter status
        """

    choice = str(input(menu))

    options = {
      '0': cli.createVoterChain,
      '1': cli.checkToken,
      '2': cli.putToken,
      '3': cli.checkVoter,
    }

    options[choice]()
