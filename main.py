import chainFunctions as cf

menu ="""select your choice:
    0) Create a chain
    1) Update a chain
    2) Query a chain
    """

choice = input(menu)

options = {
  '0': cf.createChain,
  '1': cf.updateChain,
  '2': cf.queryChain
}

options[choice]()
