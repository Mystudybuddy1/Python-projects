# What is the purpose of the constructor in the Car, Boat, and Plane classes?
# How many attributes does each object (Car, Boat, Plane) have?
# What happens if you remove the _init_ method from a class?
# Write a class Train with attributes brand and model and a method move() that prints "Slide!"What is the purpose of the constructor in the Car, Boat, and Plane classes?
# Write a class Train with attributes brand and model and a method move() that prints "Slide!"

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

class Train:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model

  def move(self):
    print("slide!")


car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object


for x in (car1, boat1, plane1):
  x.move()