import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    name = input("Please enter your name: ")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        password = generate_password(length)
        print("Generated Password:", password)
        choice = input("Do you accept this password? (yes/no/reset): ").lower()
        if choice == "yes":
            print("Thank you, {}! Your password has been generated successfully.".format(name))
            break
        elif choice == "no":
            print("Password rejected. Generating a new one...")
        elif choice == "reset":
            print("Password reset. Generating a new one...")
        else:
            print("Invalid choice. Please enter 'yes', 'no', or 'reset'.")

if _name_ == "_main_":
    main()