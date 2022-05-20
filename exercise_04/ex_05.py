print("GRADES")

def computegrade(grade):
    s=""
    if float(grade) > 1.0:
        print("ERROR! Type a grade from 0.0 to 0.9.")
    elif grade >= 0.9:
        return "A"
    elif grade >= 0.8:
        return "B"
    elif grade >= 0.7:
        return "C"
    elif grade >= 0.6:
        return "D"
    elif grade < 0.6:
        return "F"


try:
       g = float(input("What was your grade?\n [0.0 - 0.9]\n"))
except:
        print("ERROR! Bad grade. Type a numerical grade from 0.0 to 0.9.")


print(computegrade(g))
