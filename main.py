import encode as enc
import decode as dec


def main():
    while True:
        print("Menu\n-------------\n 1. Encode\n 2. Decode\n 3. Quit\n")

        menu_choice = input("Please enter an option:")

        if menu_choice == '1':
            password = input("Please enter your password to encode:")
            encoded_password = enc.encode(password)
            print("Your password has been encoded and stored!\n")
        elif menu_choice == '2':
            try:
                print(f"The encoded password is {encoded_password}, and the original password is {password}\n")
            except:
                print("Looks like you haven't encoded a password yet!\n")
        elif menu_choice == '3':
            exit()
        else:
            print("Please enter a number between 1 and 3.")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
