numb =[]

while (True):
    n = input('Enter a number: ')
    if n == 'done':
        print(numb)
        print('Biggest number: ',max(numb))
        print('Smallest number: ',min(numb))
        gg = []
        for item in numb:
            gg.append(float(item))
        print('The sum of the numbers in the list is: ',float(sum(gg))) 
        break  
    try:
        float(n)
    except:
        print('Invalid value, try a number')
        continue
    numb.append(n)