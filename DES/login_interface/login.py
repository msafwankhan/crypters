from getpass import getpass
from os import system
from time import sleep
from sys import stderr, exit

user_dict = {}
superuser = {}
flag = True

u = open("username.txt", 'r+')
z = (''.join((u.readlines())).split('\n'))
for i in z:
    k, v = (i.split(':'))
    user_dict[k] = v


def usrnm():
    return input("Username:")


def user_creator(user_type):
    flag = True

    while flag:
        user_name = user_type + usrnm()
        if user_name not in user_dict:
            while True:
                password = getpass("Enter a password: ")
                conf_pass = getpass("Please confirm your password: ")

                if password == conf_pass and len(password) > 2:
                    user_dict[user_name] = password
                    print("An account with the {0} username has been created".format(user_name.replace(user_type,"")))
                    sleep(2)
                    flag = False
                    u.write('\n' + user_name + ':' + password)
                    break
                else:
                    print("The passwords don't match, Please try again: ")
                    sleep(2)

        else:
            print("Username {0} has already been taken".format(user_name.replace(user_type,"")))


    

while True:
    try:
        system('cls')

        choice = int(
            input("Please enter the appropriate choice:\n\t1.Create a new user account\n\t2.Login\n\t3.Exit\n\n^_^:"))

        if choice == 3:
            print("Exiting...")
            sleep(1)
            exit()


        if choice == 1:

            system('cls')
            option = int(input(
                "What type of account would you like to create?\n\t1. Standard\n\t2.Super-user\n\t3.No, Thanks!\n\n^_^: "))

            if option < 0 or option > 2:
                print("\nOh... okay!")
                sleep(1)
                continue

            elif option != 2:
                user_creator('/N')


            elif option == 2:
                prot_1=input("You need to be a super-user to create an account priviliged accounts. Would you like to login as superuser(Y/N)\n\n^_^")
                if prot_1.lower()=='y':
                    user_name = '/S'+usrnm()
                    password = getpass("Password")
                    if user_name in user_dict and password == user_dict[user_name]:
                        print("Access Granted")
                        sleep(2)
                        user_creator("/S")

                    else:
                        print("Invalid Login Details")
                        sleep(2)



        elif choice == 2:
            while True:
                user_type = int(input("Enter the account type:\n\t1.Super-user\n\t2.Normal User\n\n^_^: "))
                if user_type == 1:
                    usr_typ = '/S'
                elif user_type == 2:
                    usr_typ = '/N'
                else:
                    print("Invalid entry")
                    system('cls')

                user_name = usr_typ + usrnm()
                password = getpass("Password")
                if user_name in user_dict and password == user_dict[user_name]:
                    system('cls')
                    print("Access Granted")
                    sleep(2)
                    exit(None)


                else:
                    print("Invalid Login Details")
                    sleep(2)
                    system('cls')

        u.close()

    except ValueError as v:
        stderr.write("Error encountered: " + str(v) + '\n')
        sleep(2)


    except TypeError as t:
        stderr.write("Error encountered: " + str(t) + '\n')
        sleep(2)


    except KeyboardInterrupt:
        question = input("Keyboard Intrerrupt detected... Do you wish to exit?(Y/N): ")
        if question.lower() == 'y':
            sleep(2)
            exit()
        else:
            continue