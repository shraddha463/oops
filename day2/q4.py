class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


# Creating Object
book1 = Book("Python Programming", "ABC", 500)


# Display Book Details
print("Title:", book1.title)
print("Author:", book1.author)
print("Price:", book1.price)