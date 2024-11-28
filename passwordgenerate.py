import random
import string

def generate_password(length=10):
    # Define the characters to use
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    length = input("Enter the desired password length (default is 10): ")
    
    # Set default length if no input
    if length.strip() == "":
        length = 10
    else:
        length = int(length)

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
