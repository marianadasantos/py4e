d = dict()
text = input('Enter a text file: ')

try:
    fhand = open(text,'r')
    
except:
    print('Invalid file')
    exit()

bitch = fhand.read()

for line in bitch:
    words = bitch.split()
for word in words:    
    d[word] = d.get(word, 0) + 1 
print(d)
