

class BusReservationSystem:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.reservations = {}

    # Book tickets
    def book_ticket(self):
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        seats = int(input("Enter number of seats to book: "))

        if seats <= self.available_seats:
            self.available_seats -= seats
            self.reservations[phone] = {
                "name": name,
                "seats": seats
            }

            print(" Ticket Booked Successfully!")
            print("Name :", name)
            print("Phone:", phone)
            print("Seats :", seats)
        else:
            print("Not enough seats available!")

  
    def view_seats(self):
        print(f" Available Seats: {self.available_seats}/{self.total_seats}")





    # Show all reservations
    def show_reservations(self):
        if not self.reservations:
            print("\n No reservations yet.")
        else:
            print("\n Reservation List")
            for phone, details in self.reservations.items():
                print(f"Name: {details['name']} | Phone: {phone} | Seats: {details['seats']}")


bus = BusReservationSystem(20)   

while True:
    print("\n===== BUS RESERVATION SYSTEM =====")
    print("1. Book Ticket")
    print("2. View Available Seats")
    print("3. Show Reservations")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        bus.book_ticket()

    elif choice == "2":
        bus.view_seats()

    elif choice == "3":
        bus.show_reservations()

    elif choice == "4":
        print(" Thank you for using the Bus Reservation System!")
        break

    else:
        print(" Invalid choice! Please try again.")

