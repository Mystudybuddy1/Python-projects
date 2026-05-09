import random
print("===== Password Generator =====")
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "@#$%&*!"
all_characters = letters + numbers + symbols
length = int(input("Enter password length: "))
password = ""
for i in range(length):
    password = password + random.choice(all_characters)
print("Your password is:", password)