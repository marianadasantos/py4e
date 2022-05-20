def split(word):
    return [char for char in word]

word = input('Enter a word: ')

fm = split(word)

d = dict()

print(fm)

for key in fm:
    if key not in d:
        d[key] = 1
    else:
        d[key] +=1
    

print(d) 