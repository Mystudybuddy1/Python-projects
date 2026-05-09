# Create classes Fan, AC, and Heater.
# Each class must have a method start() that prints different messages.
# Create objects and call start() using a loop.
class fan:
    def start(self):
        print("Fan")

class ac:
    def start(self):
        print("AC")

class heater:
    def start(self):
        print("Heater")

appliances = (fan(), ac(), heater())

for item in appliances:
    item.start()
