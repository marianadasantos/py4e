import re

fhand = open('mbox-short.txt', 'r')
fhand = fhand.read()

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)