from math import sqrt

number_list = [x for x in range(1000000,10000000)]
prime_list = []


def is_prime(number):
    if number>1:
        if number == 2:
            return True
        elif number % 2 == 0:
            return False
        for n in range(3, int(sqrt(number)),2):
            if number % n == 0:
                return False
        return True
    return False

for a in number_list:
    if is_prime(a):
        prime_list.append(a)

pl = open('prime_numbers.txt','w')
for i in prime_list:
    pl.write(str(i)+'\n')
pl.close()