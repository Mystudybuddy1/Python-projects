#4.built a Vehicle Rental System that ask users which car they want by giving them choice and for how many days by applying Object-Oriented Programming concepts like classes, objects, inheritance, and modular design into a functional project with customer management, vehicle records, booking flow, and dashboard operations.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
       
class Car(Vehicle):
    def __init__(self, make, model, year, num_seats):
        super().__init__(make, model, year)
        self.num_seats= num_seats

class Customers:
    def __init__(self, email, name, phone_no):
        self.email = email
        self.name = name
        self.phone_no = phone_no
        
class RentalSystem:
    def __init__(self):
        self.vehicles = []
        self.customers = []
        self.bookings = []

print("Welcome to the Vehicle Rental System!")
rental_system = RentalSystem()
while True:
    
    print({"1": "Book a Vehicle"})
    print({"2": "Exit"})

    
    choice = input("Enter your choice: ")

    if choice == "1":
        email = input("Enter your email: ")
        name = input("Enter your name:")
        phone_no = input("Enter your phone number: ")
        customer = Customers(email, name, phone_no)
        rental_system.customers.append(customer)

        
        vehicle_name = input("Enter the name of the vehicle you want to rent: ")
        vehicle_model = input("Enter the model of the vehicle you want to rent: ")

        rental_system.vehicles.append(Car(vehicle_name, vehicle_model, 2020, 5))


    elif choice == "2":
        print("Thank you for using the Vehicle Rental System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")










    
   