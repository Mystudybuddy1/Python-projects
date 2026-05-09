# Question: Random Username Generator
# Write a Python program that generates a random username.
# The username should contain small letters and numbers only.
# Ask the user to enter the length of the username.
# Use a for loop and random.choice() to pick random characters.
# Print the generated username at the end.
import random

print("===== Random Username Generator =====")

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
all = letters + numbers
length = int(input("Enter username length: "))
username = ""

for i in range(length): 
    username = username + random.choice(all)
print("Your username is:", username)