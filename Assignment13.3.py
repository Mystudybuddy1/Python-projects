class Calculator:
    def __add_numbers(self, a, b):
        return a + b
    
    def perform_addition(self, a, b):
        result = self.__add_numbers(a, b)
        print("Sum:", result)


calc = Calculator()

calc.perform_addition(5, 7)
calc.__add_numbers(5, 7)
