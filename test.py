import registrationFunctions as rf
import chainFunctions as cf
import time, secrets
from glossary import VA, RA
import FinalCount



entry = {
"vote" : 'newguy'
}
response = cf.updateChain(entry, "c4a852f7e5216f315093f7024b6e9f445cbce22e142de3b034b4def1834ff0bd")

print (response)
