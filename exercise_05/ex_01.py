count = 0
total = 0



while True:
    v = input("Type a number: ")
    if v == "done":
        break 
    try:
        value = float(v)
    except: 
        print("ERROR! Please, type a number\n")
        continue
    count = count + 1
    total = total + value
           
print("Count: ", count, "; Total: ", total, "; Average: ", total/count)
    



