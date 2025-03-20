import random
import string
def Create_password(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters) for i in range(length))
    return password
def main():
    try:
        length=int(input("Enter the desired length of password:"))
        if length <=0:
            print("Password length must be a positive integer.")
            return
        password=Create_password(length)
        print("Generated Password:",password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length. ")
if __name__=="__main__":
    main()