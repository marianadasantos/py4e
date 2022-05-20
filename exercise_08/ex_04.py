fname = input('File name: ')
try:
    fhand = open(fname,'r')
except:
    print('Invalid file name.')
    exit()

meme = fhand.read()

chop = meme.split() 
new_list = []
new_list = chop

for word in chop: 
    for line in new_list:
        if line not in new_list:
            new_list.append(word)

final_list = list(set(new_list))
    
final_list.sort(key = str.lower)
print(final_list)
