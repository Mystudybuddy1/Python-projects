# my7 = ("Pig", "Cow", "Dog", "Cat")
# myit = iter(my7)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# bob = "Cow"
# myit = iter("Cow")
# print(next(myit))
# print(next(myit))
# print(next(myit))
#Looping
# my7 = ("Pig", "Cow", "Dog", "Cat")
# for x in my7:
#     print(x)
# poll = "Cat"
# for x in poll:
#    print(x)

class numbers:
    def __iter__(self):
        self.a = 2
        return self
    def __next__(self):
        x = self.a 
        self.a += 2
        return x
myclass = numbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))