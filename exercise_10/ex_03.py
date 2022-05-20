import re
d = dict()
letter = list()
fname = input('Enter file: ')
try:
    fhand = open(fname,'r')
except:
    print('Invalid file')
    exit()

fhand = fhand.read()
fhand = fhand.lower()
fhand = re.sub('[^\w\s]', '', fhand)
fhand = re.sub(r'[0-9]','',fhand)
fhand = fhand.replace('_', '')
fhand = re.sub(r'\s+','',fhand)

for line in fhand:
    letter.append(line)
for let in letter:
    d[let] = d.get(let, 0) +1
t = sorted(d.items(), reverse=True) 
print(t)  
    