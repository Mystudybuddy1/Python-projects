mytuple = ("Dog","Cat","Banana","Orange",56,1.76,True,709,True)
print(mytuple)
print(len(mytuple))
print(type(mytuple))
print(mytuple[6])
print(mytuple[-2])
print(mytuple[1:5])
print(mytuple[-5:-1])
if "Aarush" in mytuple:
    print("Yes! Dog exists in the tuple")

else:
     print("No! It does not exists")

y = list(mytuple)  
y[1] = "Aarush" 
print(y)        

print(mytuple)