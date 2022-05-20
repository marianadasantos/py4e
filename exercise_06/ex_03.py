# put the code in a function
# generalize it so it accepts the strimg and letters as arguments


def count(word, know):
    for letter in word:
        i=0    
        if letter == know:
            i = i + 1
            return i


worrd =  input("Type a word: ")
knoww = input("What letter would you like to count in your word: ")

result = count(worrd,knoww)

print("There are ", result, " letters ", knoww," in ", worrd)
