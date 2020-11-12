#Task  ->To open the file name fileuse.txt and search out all the email addresses which are available in the file and count how many are there. 


filename = input("Enter the file:")
if filename == '':
    filename = 'fileuse.txt'
fh = open(filename)
lst = list()
count = 0
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[1])
    count = count + 1

print(count)
