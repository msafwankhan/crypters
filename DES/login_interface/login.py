from getpass import getpass
from os import system
import time
from sys import exit

while True:
    try:
        system('cls')

        choice = int(input("Please enter the appropriate choice:\n1.Create a new user account\n2.Login\n#-#:"))

        normal_user = {}
        superuser = {}
        flag = True

        u = open("username.txt", 'r+')
        z=(''.join((u.readlines())).split('\n'))
        for i in z:
            k,v = (i.split(':'))
            normal_user[k] = v

        print(normal_user)


        def usrnm():
            return input("Username:")


        if choice == 1:
            while flag:
                user_name = usrnm()
                if user_name not in normal_user:
                    while True:
                        password = getpass("Enter a password: ")
                        conf_pass = getpass("Please confirm your password: ")

                        if password == conf_pass and len(password) > 2:
                            normal_user[user_name] = password
                            print("An account with the {0} username has been created".format(user_name))
                            flag = False
                            u.write('\n'+user_name+':'+password)
                            break
                        else:
                            print("The passwords don't match, Please try again: ")


                else:
                    print("Username {0} has already been taken".format(user_name))



        elif choice == 2:
            while True:
                user_name = usrnm()
                password = getpass("Password")
                print(normal_user)
                if user_name in normal_user and password == normal_user[user_name]:
                    print("access granted")
                else:
                    print("invalid login details")


        u.close()


    except KeyboardInterrupt:
        question = input("Keyboard Intrerrupt... Do you wish to exit?(Y/N): ")
        if question.lower() == 'y':
            time.sleep(2)
            exit()
        else:
            continue