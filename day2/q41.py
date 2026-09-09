class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)

    def perimeter(self):
        print("Perimeter:", 2 * (self.length + self.width))

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)


# Create object
rectangle1 = Rectangle(10, 5)

# Call methods
rectangle1.display()
rectangle1.area()
rectangle1.perimeter()