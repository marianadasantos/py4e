# create a tranversal loop that reads backwards
# if len(fruit) is 6, the count of i has to reach 6 and the word has to be printed backwards

fruit = 'banana'
i = 1
lenght = len(fruit)
while i <= lenght: 
    hey = fruit[lenght-i]
    print(hey)
    i=i+1
 
