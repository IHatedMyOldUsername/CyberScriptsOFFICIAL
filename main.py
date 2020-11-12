import functs

fakelist = ['jonah', 'fakeuser']
usersInSudo = functs.sudolist()
for user in usersInSudo:
    if(user not in fakelist):
        print(user)
        functs.remuseradmin(user)

for user in fakelist:
    if(user not in usersInSudo):
        print(user)
        functs.adduseradmin(user)
