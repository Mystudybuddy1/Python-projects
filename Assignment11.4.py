# Create a class Person with attributes name and age.
# Create a child class Employee that uses super()._init_(name, age)
# Add another attribute salary inside Employee.
# Create an Employee object and print name, age, salary.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name,age)
        self.salary = salary


n = Employee("Bob", 34, 70000)

print("Name:", n.name)
print("Age:", n.age)
print("Salary:", n.salary)
