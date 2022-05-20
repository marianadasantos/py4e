biggest = None
smallest = None
total = 0
count = 0
e = 0
o = 0

while True:
    v = input("Type a number: ")
    if v == "done":
        break
    try:
        value = float(v)
    except:
        print("ERROR! Please type a numeric value\n")
        continue
    count = count +1
    total = total + value
    if value%2 == 0:
        even = value
        e = e + 1
        print("EVEN: ",even)
    elif value%2 != 0:
        odd = value
        o = o + 1
        print("ODD: ",odd)
    if biggest == None or value>biggest:
        biggest = value
    if smallest == None or value<smallest:
        smallest = value
    
print(e," even numbers; ", o," odd numbers.\n" "The biggest value was: ", biggest, ".\n The smallest value was: ", smallest,".\n There were added ", count, " numbers. The summing of the added values is: ", total, ".")


