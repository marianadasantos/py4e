fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

#counts is a dictionary
counts = dict()
#loop to read each line
for line in fhand:
    #separate each line in words
    #put the separate words in a variable
    words = line.split()
    #loop each word in the list of words
    for word in words:
        #if the word in the list is not inside the dictionary "counts"
        if word not in counts:
            #the value of the word is 1
            counts[word] = 1
        #if it is already in the dict
        else:
            #you add 1 to the existing value
            counts[word] +=1
print(counts)

