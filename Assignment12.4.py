# Create classes CreditCard, UPI, and Cash.
# Each class must have a method pay() that prints how the payment is done.
# Call the pay() method on each object through a loop
class CreditCard:
    def pay(self):
        print("PAYEMENT WAS DONE USING THE CREDIT CARD")

class UPI:
    def pay(self):
        print("PAYMENT WAS DONE USING UPI.")

class Cash:
    def pay(self):
        print("PAYMENT WAS DONE USING CASH ")

payments = [CreditCard(), UPI(), Cash()]

for payment in payments:
    payment.pay()

