print("GRADES")

g = input("What was your grade?\n [0.0 - 0.9]\n")
try:
        grade = float(g)
except:
        print("ERROR! Bad grade. Type a numerical grade from 0.0 to 0.9.")

if (grade) > 1.0:
    print("ERROR! Type a grade from 0.0 to 0.9.")
elif grade >= 0.9:
    print("A")
elif grade >= 0.8:
    print("B")
elif grade >= 0.7:
    print("C")
elif grade >= 0.6:
    print("D")
elif grade < 0.6:
    print("F")

