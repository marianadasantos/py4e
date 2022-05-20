print("HOURLY PAY")
hours = input("How many hours do you work per week? ")
rate = input("What's the rate? ")

if float(hours) > 40:
    plus = float(hours) - 40
    times = float(rate) * 1.5
    pay = 40 * float(rate) + float(times) * float(plus)
    print("PAY:", pay)
else:
    pay = float(hours) * float(rate)
    print("PAY:", pay)