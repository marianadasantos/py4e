print("HOURLY PAY")

def computepay(a,b):
    print(a,b)
    if float(a) > 40:
        plus = float(a) - 40
        times = float(b) * 1.5
        pay = 40 * float(b) + float(times) * float(plus)
        
    else:
        pay = float(a) * float(b)
    
    return pay

try:
    h = input("How many hours do you work per week? ")
    hours = float(h)
    r = input("What's the rate? ") 
    rate = float(r)
except:
    print("ERROR! Please, enter a numeric input")
    quit()

res = computepay(hours, rate)    
print("PAY:", res)