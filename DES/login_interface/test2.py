from getpass import getpass

user_dict = {}

u = open("username.txt", 'r+')
z = (''.join((u.readlines())).split('\n'))
for i in z:
    k, v = (i.split(':'))
    user_dict[k] = v
    print(k[0:2])

def file_writer(user_name,password):
    u.write('\n' + user_name + ':' + password)



def superuser_checker(user_name):
    if user_name in user_dict and user_name[0:2] == '/S':
        return True
    else:
        return False


def dict_update:
    print(user_dict)