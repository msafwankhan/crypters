from random import choice

keys = {}

with open('pim.txt') as f:
    z = f.readlines()
    for i in range(3):
        x, y = int(choice(z)), int(choice(z))
        public_key = x * y
        name = 'K' + str(i + 1)
        keys[name] = public_key

f.close()



def EK1(dat):
    return dat * keys['K1']


def EK2(dat):
    return dat * keys['K2']


def EK3(dat):
    return int(dat * keys['K3'])


def DK1(dat):
    return dat / keys['K1']


def DK2(dat):
    return dat / keys['K2']


def DK3(dat):
    return dat / (keys['K3'])

