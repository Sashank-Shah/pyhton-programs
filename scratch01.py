#TASK-> T0 count how many times an item has occured in the list. And using get method.

count = dict()
names = ['raju', 'molu', 'solu', 'ghoku', 'molu', 'raju']

for name in names:
    if name not in count:
        count[name] = 1
    else:
        count[name] = count[name] + 1

print(count)

#The above code can be simplified using get(key, default)

for name in names:
    count[name] = count.get(name, 0)

print(count)

z= list(input("Enter lst"))
print(z)
