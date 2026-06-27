class Library:
    def __init__(self, bookissue, bookgiven, students):
        self.bookissue = []
        self.bookgiven = []
        self.students = []

class Students:
    def __init__(self, name, classname):
        self.name = name
        self.classname = classname

library = Library()
print("Welcome to the Library")
while True:
    print({"1":"Register"})
    print({"2":"Issue a book"})
    print({"3":"Return a book"})
    print({"4": "Exit"})

    choice = input("Which choice do you want to pick? ")

    if choice == "1":
        name = input("Enter your name: ")
        classname = input("Enter your class: ")

        lib = Students(name, classname)

        library.students.append(lib)

    elif choice == "2":
        bookissue = input("Which book do you wanna issue: ")

        library.bookissue.append(bookissue)
         

    elif choice == "3":

        bookgiven = input("Which book do you want to return: ")

        if bookgiven in library.bookissue:
            library.bookissue.remove(bookgiven)
            print("Book returned")
        else:
            print("You dont have this book!")

    elif choice == "4":
        print("Thank you")

    else:
        print("Invalid choice")

    

