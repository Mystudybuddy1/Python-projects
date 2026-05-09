# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)


# x = Person("John", "Doe")
# x.printname()


#Second method-->

# class Student(Person):
#   pass
# x = Student("Mike", "Olsen")
# x.printname()
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)
#Graduation Year
class Student(Person):
  def __init__(self, fname, lname, graduationyear):
    super().__init__(fname, lname)
    self.graduationyear = graduationyear

  def welcome(self): 
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Mike", "Olsen", 2019)
print(x.firstname, x.lastname, x.graduationyear)
x.welcome()