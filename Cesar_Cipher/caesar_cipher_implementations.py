from string import *

alphabet = [x for x in ascii_lowercase]
flag = 1


while flag == 1:
	oper = int(input("\nWhat would you like to do today?\n1> Encrypt\n2> Decrypt\n3> Exit\n\n>"))

	if oper == 1:
		cipher_text = []
		plain_text = input("Enter the sting to encrypt: ").lower()


		if plain_text!="":
		    option = int(input("How would you like to encrypt this message?\n\t1. Generate a string pattern\n\t2. Generate a numeric pattern\n\t\t> "))
		    while 0 < option <= 2:
		        print("Generating an encrypted message...")

		        if option == 1:
		            shift_char = int(alphabet.index(input("Enter the shift character for 'A': ").lower()))
		 			#remove the hash from the next line to dsplay the letter associations
		            #print("".join(alphabet)+"\n"+"|"*26+"\n"+"v"*26+"\n"+"".join([alphabet[(alphabet.index(x)+shift_char)%26] for x in alphabet]))
		            for a in plain_text:
		                if a == " ":
		                    cipher_text.append(a)
		                elif a !=" ":
		                    cipher_text.append(alphabet[(alphabet.index(a)+shift_char)%26])
		            print("The generated cipher text is: ".join(cipher_text))
		            break


		        elif option ==  2:
		            shift_val = int(input("Enter the shift value: "))
		            for a in plain_text:
		                if a == " ":
		                    cipher_text.append(a)
		                elif a != " ":
		                    cipher_text.append(str((alphabet.index(a) + shift_val) % 26))
		                    h = [str(len(x)) for x in cipher_text]
		            print("The generated cipher text is: {0} and the hash is: {1}".format("".join(cipher_text),"".join(h)))
		            break



	elif oper == 2:
		cipher_text = input("Enter the cipher text> ")
		checker = cipher_text.replace(" ","")
		plain_text = []

		if checker.isalpha(): 
			key = input("Enter the key value for the encryption ").lower()
			if key.isalpha() and len(key)==1:
				for char in cipher_text:
					if char not in "!@#$%^&*() ":
						plain_text.append(alphabet[(alphabet.index(char)-alphabet.index(key))%26])
					else: plain_text.append(char)
				print("\nThe decrypted message is> ","".join(plain_text))

		elif checker.isnumeric():
			key = int(input("Enter the decryption key: "))
			h = input("Enter the hash: ")
			plain_text = []
			pointer = 0
			for _ in h:
					num = ""
					for x in range(int(_)) :
						num += checker[pointer]
						pointer+=1
					plain_text.append(ascii_lowercase[((int(num))-key)%26])

			print("\nThe decoded message is: ","".join(plain_text))



	elif oper == 3:
		print("\n"+"- "*5+"Good Bye!"+" -"*5+"\n")
		flag = 0
		break
