who = dict()
nme = list()
fhand = open('mbox-short.txt','r')
for line in fhand:
    line = line.rstrip()
    if len(line) != 0 and line.startswith('From '):
        words = line.split()
        words = words[1]
        emails = words.split('@')[1]
    else:
        continue
    who[emails] = who.get(emails, 0) + 1 
print(who)
for name,numb in who.items():
    nme.append((name,numb))
print(nme)