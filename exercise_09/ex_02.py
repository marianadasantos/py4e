fhand = open('mbox-short.txt','r')
week_days = dict()
for line in fhand:
    line = line.rstrip()
    if len(line) != 0 and line.startswith('From '):
        words = line.split()
    else:
        continue
    week_days[words[2]] = week_days.get(words[2], 0) +1

print(week_days) 

#you can also use the loop:
    #for days in words:
#       if words[2] not in week_days:
#           week_days[words[2]] = 1
#       else:
#           week_days[words[2]] += 1