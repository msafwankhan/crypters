from scrambler import scrambler
from keygen import *


def cipher(*args):
    cipher_text = EK3(DK2(EK1(scrambler())))
    return cipher_text


def plain(*args):
    plain_text = round(DK1(EK2(DK3(cipher_text))))
    return plain_text


print(plain(int(input("Enter a value to generate plaintext value: "))))
