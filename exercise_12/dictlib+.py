import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = dict()
for line in fhand:
    words = line.decode().split()
    print(words)
    words = [str.lower(x) for x in words]
    for word in words:
        count[word] = count.get(word, 0) +1
print(count)