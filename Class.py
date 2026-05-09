# class numbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a 
#         self.a += 1
#         return x
# myclass = numbers()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# class persons:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = persons("aarush",36)
# print(p1.name)
# print(p1.age)

# class Calculator:
#     def add(self, a, b):
#         return a + b
#     def multiply(self, a, b):
#         return a * b
# calc = Calculator()
# print(calc.add(5, 3))
# print(calc.multiply(4, 7))
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"
p1 = Person("arush", 16)
print(p1)
