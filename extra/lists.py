lucky_numbers = [5,3,2,10,88,7]
friends = ['Kevin','Jane', 'Mimi', 'Kichi', 'Kichi', 'Oscar', 'Jules']

#adds a list to another list
friends.extend(lucky_numbers)
print(friends)

#adds an item to the end of the list
friends.append('Bob')
print(friends)

#adds an item in the middle of the list
friends.insert(1, 'Kelvin')
print(friends)

#removes items
friends.remove('Jane')
print(friends)

#removes all the items
friends.clear()
print(friends)

#pop an item from the list (the end of it i guess)
friends.pop()
print(friends)

#check if an specific item in in the list
print(friends.index('Mimi'))

#counts the number os similar elements in the list
print(friends.count('Kichi'))

#sort in ascending order (aplhabetical order)
friends.sort()
print(friends)

#sort in ascending order (ascending numbers)
lucky_numbers.sort()
print(lucky_numbers)

#reverse the list
lucky_numbers.reverse()
print(lucky_numbers,'\n')

#sort in descending order
lucky_numbers.sort(reverse=False)
print(lucky_numbers)

#copy list
friends2 = friends.copy()
print(friends2)