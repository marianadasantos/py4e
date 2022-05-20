#structure where you can store different pieces of info
#tuples are immutable

coordinates = (4, 5)

#access throuhg index: 4 is index position 0/ 5 is index position 1
print(coordinates[0])

#list of tuples
coordinates2 = [(4,5), (7,0), (5,2)]
#finding the tuple in the list. it is only possible because unlike dictionaries, list have fixed index
print(coordinates2[2])