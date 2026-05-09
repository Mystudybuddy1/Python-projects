#Calculator
class calculator:
        def add(self, a, b):
            return a + b
         
        def multiply(self, a, b):
            return a * b
        
        def divison(self, a, b):
            return a / b
        
        def substraction(self, a, b):
            return a - b
        
        
calc = calculator()
print(calc.add(7, 3))
print(calc.multiply(2, 6))
print(calc.divison(10, 5))
print(calc.substraction(7, 0))