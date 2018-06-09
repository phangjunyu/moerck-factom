import cli

menu ="""select your choice:
    0) Create a chain
    1) Update a chain
    2) Query a chain
    """

choice = input(menu)

options = {
  '0': cli.createVote,
  '1': cli.update,
  '2': cli.query
}

options[choice]()
