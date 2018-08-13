from getpass import getpass
from os import system
import csv

system('cls')

#choice = int(input("Please enter the appropriate choice:\n1.Create a new user account\n2.Login\n#-#:"))

normal_user = {}
superuser = {}
flag = True

u = open("username.txt", 'r+')
print((''.join(u.readlines())))


print(normal_user)

'''
def user_name():
    return input("Username:")


if choice == 1:
    while flag:
        user_name = user_name()
        if user_name not in normal_user:
            while True:
                password = getpass("Enter a password: ")
                conf_pass = getpass("Please confirm your password: ")

                if password == conf_pass and len(password) > 2:
                    normal_user[user_name] = password
                    print("An account with the {0} username has been created".format(user_name))
                    flag = False
                    u.write(user_name + ',' + password + '\n')
                    break
                else:
                    print("The passwords don't match, Please try again: ")


        else:
            print("{0} already taken".format(user_name))



elif choice == 2:
    user_name = user_name()
    password = getpass("Password")
    print(normal_user)
    if user_name in normal_user and password == normal_user[user_name]:
        print("access granted")
    else:
        print("invalid login details")

u.close()
'''