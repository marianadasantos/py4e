fname = input("Enter the name of the file: ")
try:
    fhand = open(fname)
except:
    print("Invalid file")
    exit()
for up in fhand:
    upp = up.upper()
    print(upp)