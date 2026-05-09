# Override move() in Car to print "Drive!" instead of using the base method.
# Add a new method honk() in Car that prints "Beep!" (but don’t call honk() in the polymorphic loop yet

class Car:
    def move(self):
        print("Drive")

    def honk(self):
        print("Beep")


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
      
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")     
train1 = Train("Vande", "Bharat")
bike1 = Bike("Shadow", "Rider")

for x in ( boat1, plane1, train1, bike1):
  x.move()
