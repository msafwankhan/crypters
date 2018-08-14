def dict_update():
    u = open("username.txt", "w")
    for k, v in user_dict.items():
        u.write(k + ':' + v)


user_dict = {}

u = open("username.txt", 'r+')

z = (''.join((u.readlines())).split('\n'))

while True:
    for i in z:
        try:
            k, v = (i.split(':'))
            user_dict[k] = v
            u.close()
        except ValueError:
            if i == '\n':
                z.remove(i)
