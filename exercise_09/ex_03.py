emails = dict()

fhand = open('mbox-short.txt', 'r')

for line in fhand:
    line = line.strip()
    if len(line) != 0 and line.startswith('From '):
        words = line.split()
    else: 
        continue
    emails[words[1]] = emails.get(words[1], 0) +1
print(emails)