print("TEMPERATURE CONVERTER")

conv = input("What type of conversiom would you like to make:\n a) °C-°F\n b) °F-°C\n")

celcius = 0
farenheit = 0

if conv == "a":
    celcius = input("What temperature in °C would you like to convert? ")
    try:
        temp = float(celcius) * 1.8 + 32
        print("The temperature is:", temp,"°F")
    except:
        print("Enter a number")
elif conv == "b":
    farenheit = input("What temperature in °F would you like to convert? ")
    try:
        temp = (float(farenheit) - 32) / 1.8
        print("The temperature is:", temp,"°C")
    except:
        print("Enter a number")
else:
    print('ERROR')

