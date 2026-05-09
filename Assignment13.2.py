class BankAccount:
    def __show_balance(self):
        print("Your balance is confidential")

    def display(self):
        self.__show_balance()


account = BankAccount()
account.display()
