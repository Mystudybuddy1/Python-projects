class Books:
    def __init__(self, booktitle, bookauthor):
        self.booktitle = booktitle
        self.bookauthor = bookauthor

    def __str__(self):
        return f"{self.booktitle} ({self.bookauthor})"
p1 = Books("The Great Gatsby", "F. Scott Fitzgerald")
print(p1)
