#greedy matching
import re
x = 'From: Using the : character'
print(x,'\n')
y = re.findall('^F.+:', x)
print('greedy mathcing\n')
print(y,'\n')


#non greedy mathcing
y = re.findall('^F.+?:', x)
print('non-greedy matching\n')
print(y)
