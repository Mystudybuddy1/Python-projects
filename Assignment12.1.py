# Write a Python program that creates three classes: Dog, Cat, and Cow.
# Each class should have a constructor that stores the animal's name and a method sound() that prints the sound of that animal.
# Create one object of each class and call their sound() method inside a loop
class dog:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} Bark")

class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} Meow")

class cow:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} Moooo")

dog = dog("Tommy")
Cat = Cat("Mickey")
cow = cow("Farry")
am = [dog, Cat, cow]
for animal in am:
    animal.sound()

