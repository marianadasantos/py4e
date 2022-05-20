import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    y = re.findall('^From .* ([0-9][0-9]):', line)
    if len(y)>0:
        print(y)

