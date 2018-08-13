
from Cesar_Cipher.caesarcipher import caesarcipher


with open('cryptme.txt') as f:
    s = f.read().lower()

buffer = s

for _ in range(6):
    buffer = caesarcipher(buffer)




c = open('crypted.txt','w')
c.write(buffer)
c.close()