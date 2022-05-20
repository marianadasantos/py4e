#FINE TUNING STRING EXTRACTION
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
print(x,'\n')

y = re.findall('\S+@\S+', x)
print('\S+@\S+'', x')
print('non white space + @ + non white space')
print(y,'\n')

#PARENTHESES
#finds it using the start of the line, but the answer doesn't include the start of the line

y = re.findall('^From (\S+@\S+)', x)
print('^From (\S+@\S)'', x')
print('finds it using the start of the line, but the answer does not include the start of the line')
print(y)





