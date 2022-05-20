word = 'music'
guess = ''
count_times = 0
max_times = 3
enough_times = False

while guess != word and not (enough_times):
    if count_times < max_times:
        guess = input('Try a word: ')
        count_times +=1
    else:
        enough_times = True

if enough_times:
    print('You lost, mate!')
else:
    print('You WON, mate!')