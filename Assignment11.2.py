class person:
    def __init__(self, name):
        self.name = name

class Teacher(person):
    pass

class Student(person):
    pass

teacher = Teacher("Miss Poppy")
student = Student("John")
print(teacher.name)
print(student.name)

