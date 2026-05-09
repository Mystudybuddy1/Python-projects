# Create two more subclasses of Vehicle:
# Bike that overrides move() → prints "Ride!"
# Train that overrides move() → prints "Choo-choo!"
# Instantiate them and add to the same loop
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
    print("Choo Choo!")

class Bike:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model

  def move(self):
      print("Ride")

car1 = Car("Ford", "Mustang")       
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")     
train1 = Train("Vande", "Bharat")
bike1 = Bike("Shadow", "Rider")

for x in (car1, boat1, plane1, train1, bike1):
  x.move()