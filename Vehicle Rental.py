class Vehicles:
    def __init__(self, name, model):
        self.name = name
        self.model = model

class Car(Vehicles):
    def __init__(self, name, model, seats):
        super().__init__(name, model)
        self.seats = seats

class Customers:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Rentalsystem:
    def __init__(self, customer=None, history=None, cars=None):
        self.customer = customer if customer is not None else []
        self.history = history if history is not None else []
        self.cars = cars if cars is not None else []

class Summary:
    def __init__(self, history):
        self.history = history

    def show(self):
        print("Your history is:")
        for i in self.history:
            print(i)

rentalsystem = Rentalsystem()

print("Menu")
while True:
    print({"1": "Create a Rental account"})
    print({"2": "Rent a car"})
    print({"3": "Summary"})
    print({"4": "Exit"})

    choice = input("Pick your choice..")

    if choice == "1":
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")

        customer = Customers(name, email, phone)
        rentalsystem.customer.append(customer)
        rentalsystem.history.append(f"Account created for {name}")

    elif choice == "2":
        car_name = input("Enter your car name: ")
        model = input("Enter your car model: ")
        seats = input("Enter number of seats: ")

        car = Car(car_name, model, seats)
        rentalsystem.cars.append(car)
        rentalsystem.history.append(f"Car rented: {car_name} {model}")

    elif choice == "3":
        summary = Summary(rentalsystem.history)
        summary.show()
        
    elif choice == "4":
        print("Thanks for using")
        break
    else:
        print("Invalid choice")



    
        
