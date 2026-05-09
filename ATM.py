
class ATM:
    def __init__(self):
        self.pin = None
        self.balance = 0

    def set_pin(self):
        while True:
            new_pin = input("Set a 4-digit PIN: ")
            if new_pin.isdigit() and len(new_pin) == 4:
                self.pin = new_pin
                print("PIN set successfully!")
                break
            else:
                print("Invalid PIN. Please enter a 4-digit number.")

    def verify_pin(self):
        if self.pin is None:
            print("No PIN set. Please set a PIN first.")
            return False

        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN. Access denied.")
            return False
        
    def check_balance(self):
        if self.verify_pin():
            print(f"Your current balance is: {self.balance}")

    def deposit(self):
        if self.verify_pin():
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                self.balance += amount
                print(f"{amount} deposited successfully! New balance: ${self.balance}")
            else:
                print("Invalid amount. Please enter a positive number.")
    
    def withdraw(self):
        if self.verify_pin():
            amount = float(input("Enter amount to withdraw: "))
            if amount > 0:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"{amount} withdrawn successfully! New balance: {self.balance}")
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid amount. Please enter a positive number.")
    
atm = ATM()
while True:
    print("===== ATM SYSTEM =====")
    print("1. Set PIN")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        atm.set_pin()
    elif choice == "2":
        atm.check_balance()
    elif choice == "3":
        atm.deposit()
    elif choice == "4":
        atm.withdraw()
    elif choice == "5":
        print("Thank you for using the ATM system!")
        break
    else:
        print("Invalid choice! Please try again.")


