import cli

menu ="""select your choice:
    0) Registration Booth
    1) Voting Booth
    """

choice = input(menu)

if choice == '0':
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
else:
    menu ="""select your choice:
        0) Register
        1) Check Tokens
        """

    choice = input(menu)

    options = {
      '0': cli.createVoter
      '1': cli.checkTokens,
      # '1': cli.putRA,
      # '2': cli.putVA,
    }

    options[choice]()
