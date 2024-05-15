import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length must be a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    password = generate_password(length)
    print("Generated Password:", password)

if __name__== "_main_":
    main()