storage = dict()

words = open('words.txt', 'r')
words = words.read()
words = words.lower()
words = words.split()

storage = dict.fromkeys(words, " ")

print(type(storage))

print(storage)

while (True):
    is_it = input('Look up a word in the dictionary: ')
    
    if is_it == 'done':
        break

# qualquer input é string, por isso try n faz sentido aqui, mor
#    try:
#        str(is_it)
#    except:
#        print("Invalid input. Try a word.")
#        continue
    
    print("'",is_it.capitalize(),"' in the dictionary:")
    
    if is_it in storage:
        print('True')
    else:
        print('False')

