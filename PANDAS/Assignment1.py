#  ============================================================
#        PYTHON HOMEWORK ASSIGNMENT - Mini Bank System
# ============================================================
#
# OBJECTIVE:
#   Build a simple Bank Account system using Python.
#   This project will test your knowledge of:
#     - Variables & Data Types
#     - Input / Output
#     - If-Else Conditions
#     - Loops (while)
#     - Lists & Dictionaries
#     - Functions
#     - String formatting
#     - OOPs (Classes & Objects)
#
# ============================================================
#
# INSTRUCTIONS:
#
# 1. Create a class called "BankAccount" with:
#      - Attributes: account_holder (str), balance (float), transaction_history (list)
#      - Methods:
#          a) deposit(amount)   -> adds money, prints new balance, saves to history
#          b) withdraw(amount)  -> removes money if enough balance, else print error
#          c) check_balance()   -> prints current balance
#          d) show_history()    -> prints all past transactions
#          e) display_info()    -> prints account holder name and balance
#
# 2. Create a menu-driven program using a while loop:
#      Menu:
#        1. Create Account
#        2. Deposit Money
#        3. Withdraw Money
#        4. Check Balance
#        5. Transaction History
#        6. Account Info
#        7. Exit
#
# 3. Use if-elif-else to handle menu choices.
#
# 4. Use input() to take user choices and amounts.
#
# 5. Handle errors:
#      - Don't allow negative deposits
#      - Don't allow withdrawal more than balance
#      - Show message if account not created yet
#
# ============================================================
#
# EXAMPLE OUTPUT:
#
#   ===== Mini Bank System =====
#   1. Create Account
#   2. Deposit Money
#   3. Withdraw Money
#   4. Check Balance
#   5. Transaction History
#   6. Account Info
#   7. Exit
#   Enter your choice: 1
#   Enter your name: Arush
#   Account created for Arush with balance 0.
#
#   Enter your choice: 2
#   Enter deposit amount: 500
#   Deposited 500. New balance: 500
#
#   Enter your choice: 3
#   Enter withdrawal amount: 200
#   Withdrawn 200. New balance: 300
#
#   Enter your choice: 5
#   --- Transaction History ---
#   1. Deposited: +500
#   2. Withdrawn: -200
#
# ============================================================
#
# WRITE YOUR CODE BELOW:
# ============================================================


class bankaccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0
        self.transaction_history = []
    def deposit(self, amount):
        try:
           
            if amount > 0:
                self.balance += amount
                self.transaction_history.append(f"Deposited: +{amount}")
            else:
                print("Please enter a proper amount")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def withdraw(self, amount):
        
        if amount <= 0:
            print("Please enter a positive amount")
        
        elif amount > self.balance:
            print("Amount exceeds balance. Withdrawal failed.") 
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: -{amount}")


    def check_balance(self):
        print(f"Your Balance is: {self.balance}")

    def show_history(self):
        print("Your Transaction History:")
        for i,transaction in enumerate(self.transaction_history):
            print(f"{i}. {transaction}")
    
    def display_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")

    def menu(self):
        while True:
            print("===== Mini Bank System =====")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Account Info")
            print("7. Exit")
        
            choice = input("Enter your choice: ")
            if choice == "1":
                name = input("Enter your name: ")
                self.__init__(name)
                print(f"Account created for {name} with balance 0.")

            elif choice == "2":
                if self.account_holder:
                    try:
                        amount = float(input("Enter deposit amount: "))
                        self.deposit(amount)
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")
                else:
                    print("Please create an account first.")

            elif choice == "3":
                if self.account_holder:
                    try:
                        amount = float(input("Enter withdrawal amount: "))
                        self.withdraw(amount)
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")
                else:
                    print("Please create an account first.")

            elif choice == "4":
                if self.account_holder:
                    self.check_balance()
                else:
                    print("Create an account please...")
                
            elif choice == "5":
                if self.account_holder:
                    self.show_history()
                else:
                    print("Create an account please...")

            elif choice == "6":
                if self.account_holder:
                    self.display_info()
                else:
                    print("Please create an account...")

            elif choice == "7":
                print("Thank you")
                break

            else:
                print("Invalid choice. Please try again.")



bank = bankaccount("")
bank.menu()





