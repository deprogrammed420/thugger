import random

IME_FILE='vsi_verzi.txt'

def thugger():
    with open(IME_FILE,'r') as file:
        verzi=file.readlines()
        verzi_brezvrstic=[line.rstrip('\n') for line in verzi]
        return verzi_brezvrstic[random.randint(0,len(verzi_brezvrstic))]


