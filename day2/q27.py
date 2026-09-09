class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_book(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


# Create object
book1 = Book("Python Programming", "John Smith", 500)

# Display book details
book1.display_book()