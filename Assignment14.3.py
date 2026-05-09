# Write a program to count how many words are present in a file.

with open("data.txt", "r") as file:
    g = file.read()          
    words = g.split()       
    wordnum = len(words)      
print(wordnum)
