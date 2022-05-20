def split(word):
    return [char for char in word]

word = input('Enter a word: ')

fm = split(word)

d = dict()

print(fm)

for key in fm:
    d[key] = d.get(key, 0) + 1
    
print(d) 