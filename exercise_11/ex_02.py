import re 
numlist = list()
fname = input('Enter a file: ','r')
hand = open(fname)
soma = 0
vezes = 0
for line in hand:
    line = line.rstrip()
    achou = re.findall('^New Revision: ([0-9.]+)', line)
    if len(achou) < 1: continue
    numeros = float(achou[0])
    numlist.append(numeros)
for num in numlist:
    soma = num + soma
    vezes = vezes+1

average = soma/vezes
print(average)

   