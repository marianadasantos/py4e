d = dict()
line = input('enter file: ')
fhand = open(line, 'r')
fhand = fhand.read()
words = fhand.split()

for word in words:
    d[word] = d.get(word, 0)+1

print(d)
