fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print("Invalid file.")
    exit()
count_spam =0
count_lines = 0
for line in fhand:
    count_lines = count_lines +1
    if line.startswith('X-DSPAM-Confidence: 0.8475'):
        new_line = line
        dd = new_line.find(' ')
    if line.startswith('X-DSPAM-Confidence:'):
        count_spam = count_spam+1
print(float(new_line[dd+1:]),'\nThere are ', count_spam,' spam confidence values.\n AVERAGE:', round(count_spam/count_lines, 3))

        
