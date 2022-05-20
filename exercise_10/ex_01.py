fhand = open('mbox-short.txt', 'r')
d = dict()

for line in fhand:
    if line[0] != 0 and line.startswith('From '):
        words = line.split()
    else: continue
    d[words[1]] = d.get(words[1], 0) + 1
print(d)

lst = list()

for email,count in d.items():
    newtup = (count,email)
    lst.append(newtup)
lst = sorted(lst, reverse=True)

print('MOST EMAILS SENT BY:',lst[0])

