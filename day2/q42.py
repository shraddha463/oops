import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area:", math.pi * self.radius * self.radius)

    def circumference(self):
        print("Circumference:", 2 * math.pi * self.radius)

    def display(self):
        print("Radius:", self.radius)


# Create object
circle1 = Circle(7)

# Call methods
circle1.display()
circle1.area()
circle1.circumference()