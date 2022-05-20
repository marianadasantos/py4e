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

smallest = None
biggest = None

for name, numbers in emails.items():
    if smallest is None or numbers < smallest:
        smallest = numbers
        who1 = name
    elif biggest is None or numbers > biggest:
        biggest = numbers
        who2 = name

print('Sent the most emails:', who2,':' ,biggest)
print('Sent the least emails:', who1, ':',smallest)