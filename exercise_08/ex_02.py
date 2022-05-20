fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != 'From': continue
    count = count+1
    print(words[2])
print(count)