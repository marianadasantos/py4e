print("HOURLY PAY")

def computepay(a,b):
    print(a,b)

try:
    h = input("How many hours do you work per week? ")
    hours = float(h)
    r = input("What's the rate? ") 
    rate = float(r)
except:
    print("ERROR! Please, enter a numeric input")
    quit()

computepay(hours, rate)    
if float(hours) > 40:
    plus = float(hours) - 40
    times = float(rate) * 1.5
    pay = 40 * float(rate) + float(times) * float(plus)
    print("PAY:", pay)
else:
    pay = float(hours) * float(rate)
    print("PAY:", pay)