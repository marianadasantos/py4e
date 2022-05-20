#ESCAPE CHARACTER
import re
x = 'We just receives $10.00 for cookies'
y = re.findall('\$[0-9.]+', x)
print(y)