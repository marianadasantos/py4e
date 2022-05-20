storage = dict()

with open('words.txt') as cucu:
    for line in cucu:
        line = line.rstrip()
        yess = line.split()
        storage = dict.fromkeys(yess, " ")
print(storage)