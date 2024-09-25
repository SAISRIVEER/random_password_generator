import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '^', '_', '~']

print("Welcome to the Random Password Generator by SRI VEER!")

while True:
    password_length = int(input("What's the total length of the password you're trying to set?: "))
    nr_letters = int(input("How many letters would you like in your password?: "))

    if nr_letters > password_length:
        print("You have chosen more letters than the total length of the password. Please try again.")
        continue

    if (nr_letters == password_length):
        print("Looks like your password is weak, So kindly choose some symbols and numbers also.")
        continue

    if (nr_letters < password_length):
        nr_symbols = int(input(f"How many symbols would you like in your password? (Still {password_length - nr_letters} places left): "))
        letters_and_symbols = nr_letters + nr_symbols

        if (letters_and_symbols > password_length):
            print(f"You have already choosen {nr_letters} letters and now you're choosing {nr_symbols} symbols which exceeds the total length of the password which is {password_length}.")
            continue

        elif(letters_and_symbols == password_length):
            print("Your password is good but if you add some numbers to it then it will be better, So please add some numbers to it.")
            continue

        else:
            nr_numbers = int(input(f"How many numbers would you like in your password? (Still {password_length - letters_and_symbols} places left): "))
            if (letters_and_symbols+nr_numbers>password_length):
                print(f"You have already choosen {nr_letters} letters and {nr_symbols} symbols and now you're choosing {nr_numbers} numbers which exceeds the total length of the password which is {password_length}.")
                continue
            elif(letters_and_symbols + nr_numbers==password_length):
                password_list = []
                for i in range(0, nr_letters):
                    password_list += random.choice(letters)
                for i in range(0, nr_symbols):
                    password_list += random.choice(symbols)
                for i in range(0, nr_numbers):
                    password_list += random.choice(numbers)
                
                random.shuffle(password_list)
                password = ''
                for item in password_list:
                    password += item
                print(f"Your Password is {password}")
                break
            else:
                print(f"Your selections don't fill the entire password length. You still have {password_length - (nr_letters + nr_symbols + nr_numbers)} spaces left. Please try again.")
                continue
