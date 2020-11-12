#Below is a dict containing list of persons with bank account in pnb bank(yes) and who don't have(No) with their recent deposit.
#TASK is to bring up the names of the pnb bank holders and find the average of the total recent deposit in the bank combined.

details = {'Eva': ['No', 25, 304], 'Mark': ['Yes', 21, 302], 'Jonas': ['No', 20, 334], 'James': ['Yes', 25, 124], 'Nick': ['Yes', 24, 132], }
print(details)
#lst = details.values()
#print(lst)
#for x in lst:
 #   print(x)
count = 0
temp = 0
for x,y in details.items():
    for z in y:
        if z == '' or z != 'Yes':
            continue
        print(x,z, y[2])
        temp = temp + 1
        count = count + y[2]

print(count//temp)
