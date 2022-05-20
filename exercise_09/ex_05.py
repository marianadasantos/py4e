who = dict()
nme = dict()
fhand = open('mbox-short.txt','r')
for line in fhand:
    line = line.rstrip()
    if len(line) != 0 and line.startswith('From '):
        words = line.split()
    else:
        continue
    who[words[1]] = who.get(words[1], 0) + 1 
print(who)

for name,num in who.items():
    nme[name.split('@')[1]] = nme.setdefault([name.split('@')[1]], num) + num
print(nme)

