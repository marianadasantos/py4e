import re 
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From\s.*\s.*\s.*\s[0-9]\s([0-9.]+\S*)', line)
    if len(x)>0:
        print(x)