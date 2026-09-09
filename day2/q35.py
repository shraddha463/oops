class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book(self):
        print("Book Title:", self.title)
        print("Author:", self.author)


# Create object
book1 = Book("Python Programming", "John Smith")

# Call method
book1.display_book()