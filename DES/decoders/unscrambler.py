from string import ascii_lowercase
from enchant import Dict
import itertools


def unscrambler(*value):
    value = int(input("Enter a value: "))
    alp = {x + 1: y for x, y in enumerate(ascii_lowercase)}
    splitter = [int(x) for x in str(value)]
    pot_v = [alp[i] for i in splitter]

    for i in range(len(splitter) - 1):
        fin_val = int(str(splitter[i]) + str(splitter[i + 1]))
        if fin_val <= 26:
            pot_v.append((alp[fin_val]))

    pot_v.sort()
    print(pot_v)

    str_pot_val = []
    d = Dict("en-US")

    f = open('unscrambled.txt', 'w')

    for i in range(len(pot_v)):
        for combination in set(map("".join, itertools.permutations(pot_v, i))):
            if len(combination) > 2 and d.check(combination):
                f.write(combination + '\n')
            print(combination)

    f.close()

unscrambler()