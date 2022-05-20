import re

def translate(phrase):
    x = re.sub('[AEIOU]', 'G', phrase)
    y = re.sub('[aeiou]', 'g', x)
    return y

print(translate(input('Enter a phrase: ')))

'''
def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.isupper():
            translation = translation + 'G'
        else:
            translation = translation + 'g'
    return translation

print(translate(input('Enter a phrase: ')))
'''