import random
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
num="1234567890"
symbols="!@#$%^&*()_-+={}[]:\";\"<>,.?/|\\"
password=""
word=""
Password_length=int(input("Enter the password length:"))
print("yes or no")
letter=str(input("Do you want letters in password:"))
number=str(input("Do you want numbers in password:"))
symbol=str(input("Do you want symbols in password:"))
try:
    if letter=="yes":
        word+=letters
    if number=="yes":
        word+=num
    if symbol=="yes":
        word+=symbols
        
    for a in range(Password_length):
        password+=random.choice(word)
        
    print(password)
except IndexError:
    print("Password can be made of lettres,symbols.You have to set atleast one of them.")                    