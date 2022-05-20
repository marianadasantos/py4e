import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
#STUFF SE TORNA UMA SERIE DE LISTAS COM 1 ITEM, O RE.FINDALL(...)
#NÃO SE PODE TRANSFORMAR LISTA EM FLOAT(), ENTÃO PEGA STUFF COM INDEX 0 (O PRIMEIRO E UNICO ARGUMENTO DE CADA LISTA)
#TRANSFORMA EM NUMERO E DEPOIS ADC NUMA LISTA E LÊ QUEM É O NUM MAIOR ETC
    num = float(stuff[0])
    numlist.append(num)
print(numlist)
print('Maximum:', max(numlist))