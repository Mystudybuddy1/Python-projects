# Write a program that reads a file line by line and prints each line with line numbers
# Program to read a file line by line and print each line with line numbers
with open("Data.txt", "r") as file:
    linenum = 1
    for line in file:
        print(str(linenum) + ": " + line.strip())
        linenum += 1


