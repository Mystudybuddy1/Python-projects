# Write a Python program to create a class Teacher and a class Student.
# Both should have a constructor with name and age.
# Both should have a method info() that prints "Teacher info" or "Student info".
# Create one teacher and one student object, then call their info() methods in a loop

class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Teacher info")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Student info")


teacher = Teacher("DEEPAK", 36)
student = Student("Aarush", 20)

people = (teacher, student)

for person in people:
    person.info()
