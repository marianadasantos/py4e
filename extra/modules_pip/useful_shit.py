import random

feet_in_a_mile = 52800
meters_in_kilomete = 1000
beatles = ["John Lennon", "Paul McCartney", "Gerge Harrison", "Ringo Star"]


def get_file_extent(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)


