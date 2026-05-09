
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
class electriccar(Car):
    pass

my_car = electriccar("Hyundai", "Grand i10")
print("Brand:", my_car.brand)
print("Model:", my_car.model)