class Library:
    def __init__(self):
        self.bookissue = []
        self.bookgiven = []
        self.students = []

class Student:
    def __init__(self, name, classname):
        self.name = name
        self.classname = classname

library = Library()
print("Welcome to School Library!!")
while True:

    print({"1":"Register"})
    print({"2":"Issue a book"})
    print({"3":"Return a book"})
    print({"4":"Exit"})

    choice = input("Please select a choice: ")

    if choice == "1":
        
    
        name = input(str("What is your name:  "))
        classname = input("What is your class: ")
        t = Student(name, classname)
        library.students.append(t)
    

    elif choice == "2":
        bookissue = input("Name of book you want: ")

        library.bookissue.append(bookissue)

    elif choice == "3":
        bookgiven = input("Enter the name of book you want to return: ")

        if bookgiven in library.bookissue:
            library.bookissue.remove(bookgiven)
            print("Book returned")
        else:
            print("You dont have this book!")


    elif choice == "4":
        print("Thank you!")
        break
    
    else:
        print("Invalid choice")
