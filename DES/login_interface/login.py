from getpass import getpass
from os import system
from time import sleep
from sys import stderr, exit

user_dict = {}
flag = True

u = open("username.txt", 'r')
z = (''.join((u.readlines())).split('\n'))

for i in z:
    if i != '':
        k, v = (i.split(':'))
        user_dict[k] = v
u.close()


def file_update():
    u = open("username.txt", "w")
    for k, v in user_dict.items():
        u.write(k + ':' + v + '\n')
    u.close()


def usrnm():
    return input("Username:")


def user_creator(user_type):
    flag = True

    while flag:
        user_name = user_type + usrnm()
        if len(user_name) > 0 and user_name not in user_dict:
            while True:
                password = getpass("Enter a password: ")
                conf_pass = getpass("Please confirm your password: ")

                if len(password) < 3:
                    print("Password too short")

                elif password == conf_pass and len(password) > 2:
                    user_dict[user_name] = password
                    print("An account with the {0} username has been created".format(user_name.replace(user_type, "")))
                    sleep(2)
                    flag = False
                    user_dict[user_name] = password
                    break
                else:
                    print("The passwords don't match, Please try again: ")
                    sleep(2)

        elif len(user_name) < 0:
            print("Please enter a valid username")

        else:
            print("Username {0} has already been taken".format(user_name.replace(user_type, "")))

    file_update()
    sleep(5)


def superuser_checker(user_name):
    if user_name in user_dict and user_name[0:2] == '/S':
        return True
    else:
        return False


def authenticate(user_name, password):
    if user_name in user_dict and password == user_dict[user_name]:
        system('cls')
        print("Access Granted")
        sleep(2)
        return True

    else:
        print("Invalid Login Details")
        sleep(2)
        return False


def user_delete():
    while True:
        choice = int(input("What type of account would do you have?\n1.Super-user\n2Normal User\n3.<-Back\n\n^_^: "))
        print("Please login to make changes:\n\n^_^: ")

        if choice == 3:

            break

        if choice == 2:
            user_name = '/N' + usrnm()
            password = getpass("Password")
            if authenticate(user_name, password):
                conf = input("Are you sure you want to delete the account with username {0}?(Y/N)\n\n^_^ :".format(user_name)).lower()
                if conf == 'y':
                    print("The user {0} has been deleted".format(user_dict.pop(user_name)))
                    sleep(2)
                    return False
                elif conf == 'n':
                    print('\nAccount deletion cancelled\n')
                    sleep(2)
                    continue
                else:
                    print("Please enter the correct option")
                    
            else:
                print("You can have the superuser delete the user account")
                sleep(2)

        elif choice == 1:
            user_name = '/S' + usrnm()
            password = getpass("Password")
            if authenticate(user_name, password):
                usr_typ = {1: '/N', 2: '/S',3:None}
                del_usr_type = int(input("Select the user type\n1.Normal\n2.Priviliged\n3.<-Back\n\n^_^: "))
                if del_usr_type == 3:
                    break
                del_usr_name = usr_typ[del_usr_type] + input("Enter the username of the account to be deleted")
                conf = input("The user {0} will be deleted. Are you sure? (Y/N): \n\n^_^:".format(del_usr_name)).lower()
                if conf == 'y':
                    print("The user {0} has been deleted".format(user_dict.pop(del_usr_name)))
                    sleep(2)
                    return False
                elif conf == 'n':
                    print('\nAccount deletion cancelled\n')
                    sleep(2)
                    continue
                else:
                    print("Please enter the correct option")
            else:
                print("You don't seem to have enough privileges to make changes.\n")


while True:
    try:
        system('cls')

        choice = int(
            input("Please enter the appropriate choice:\n\t1.Create a new user account\n\t2.Login\n\t3.Delete a user account\n\t4.Exit\n\n^_^:"))

        if choice == 4:
            print("Exiting...")
            sleep(1)
            exit()

        if choice == 1:

            system('cls')
            option = int(input(
                "What type of account would you like to create?\n\t1.Standard\n\t2.Super-user\n\t3.No, Thanks!\n\n^_^: "))

            if option < 0 or option > 2:
                print("\nOh... okay!")
                sleep(1)
                continue

            elif option != 2:
                user_creator('/N')


            elif option == 2:
                prot_1 = input(
                    "You need to be a super-user to create an account priviliged accounts. Would you like to login as superuser(Y/N)\n\n^_^")
                if prot_1.lower() == 'y':
                    user_name = '/S' + usrnm()
                    password = getpass("Password")
                    if authenticate(user_name, password):
                        user_creator("/S")





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
                authenticate(user_name, password)
                exit()

        elif choice == 3:
            user_delete()



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

    finally:
        file_update()
