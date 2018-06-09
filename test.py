import chainFunctions as cf
import time


entry = {
"vote" : 'newguy',
"UnixTimeSTamp": str(time.time())
}
response = cf.updateChain(entry, "c4a852f7e5216f315093f7024b6e9f445cbce22e142de3b034b4def1834ff0bd")

print (response)
