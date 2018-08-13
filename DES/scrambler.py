from string import ascii_lowercase
from copy import deepcopy


def scrambler(*plaintext):
    plaintext = input("Enter the value to scramble: ")
    alphabets = [x for x in ascii_lowercase]
    scrambled = []
    for letter in plaintext.lower():
        scrambled.append(str(alphabets.index(letter) + 1))

    scrambled_list = deepcopy(scrambled)
    print(scrambled_list)
    scrambled = int(''.join(scrambled))

    return scrambled

