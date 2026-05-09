#While loop
i = 1
while i<10:
    print(i)
    if (i==3):
        break
    i += 1
     
#Array
fruits = ["mango", "banana", "orange", "kiwi", "apple", "cherry", "blueberry", "pear", "grapes", "papaya" ]
x = fruits[7]
print(x)
fruits[7] = "cherry"

print(len(fruits))   

for x in fruits:
    print(x)

fruits.append("blueberry")
fruits.pop(1)
print(fruits)
