import csv
import os

os.system("cls")
with open('numbers.csv') as testpal1:
    readpal = list(csv.reader(testpal1, delimiter=','))


if not os.path.exists("new_prime.txt"):
    f = open("new_prime.txt",'w')
    for i in readpal:
        for j in i:
            if j == ' ':
                f.write('')
            else:
                f.write(str(j)+'\n')

    f.close()


elif os.path.exists("new_prime.txt"):
    with open("new_prime.txt") as f:


        s = f.readlines()
        for i in range(len(s)-6900):
            if s[i] == '\n':
                s.pop(i)

    f.close()

f = open("pim.txt",'w')
for o in s:
    print(o)
    f.write(str(o))

f.close()