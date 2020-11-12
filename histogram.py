#To find top five words that occur in txt file.
filename = input("Enter the file:")
#if filename == '':
 #   filename = 'asgnmtlst.txt'
fh = open(filename)
dct = dict()
count = 0
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    nw = words[5]
    pepp = nw.split(':')
    nwpepp = pepp[0]
    #print(nwpepp)
    dct[nwpepp] = dct.get(nwpepp, 0) + 1


#print(dct)
lst = list()
for k,v in dct.items():
    #print(v,k)
    newt = (v, k)
    lst.append(newt)

lst = sorted(lst)
#print("Sorted list of tuples: ", lst)

for v,k in lst:
    print(v,k)
