fhand = open('mbox-short.txt','r')
count = 0
for lulu in fhand:
    lulu = lulu.rstrip()
    if  len(lulu)<1 or not lulu.startswith('From '): continue
    mail = lulu.split()
    count=count+1
    print(mail[1])
print('There are ',count,' lines that strat with "From".')