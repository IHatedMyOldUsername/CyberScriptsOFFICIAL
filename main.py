from functs import *
import requests

url = ''

sudoList = ['jonah', 'fakeuser']
usersInSudo = functs.sudolist()
for user in usersInSudo:
    if(user not in sudoList):
        print(user)
        functs.remuseradmin(user)

for user in fakelist:
    if(user not in usersInSudo):
        print(user)
        functs.adduseradmin(user)

enableFirewall()
configureSSH()
removeUnneeded()

