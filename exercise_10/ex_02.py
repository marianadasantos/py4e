fhand = open('mbox-short.txt', 'r')
d = dict()
final = list()

for line in fhand:
    if line[0] != 0 and line.startswith('From '): 
        words = line.split()
        mimi = words[5]
        mimi = mimi[:2]
        print(mimi)
    else: 
        continue
    d[mimi] = d.get(mimi, 0) + 1

print(d)

for h, num in d.items():
    final.append((h, num))
final.sort()
for h, num in final:
    print(h,num)