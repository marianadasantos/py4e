import random 
x = random.randrange(0,10,2)
print(x)


import random
x = random.choice([1,5,4,32,"maria",55])
print(x)


import random
mylist = ['mimi', 'frank','cu', 'assss']
x = random.choices(mylist, weights = [ 3,2,1,1], k=7)
print(x)

