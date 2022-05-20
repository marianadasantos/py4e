biggest = None
smallest = None

while True:
    v = input("Type a number: ")
    if v == "done":
        break
    try:
        value = float(v)
    except:
        ("ERROR! Please, type a number\n")
        continue
    if biggest == None or value > biggest:
        biggest = value
    if smallest == None or value < smallest:
        smallest = value

print("Maximum: ", biggest, "; Minimum: ", smallest) 

    