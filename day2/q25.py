class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)


# Create object
person1 = Person("Shraddha")

# Call greet method
person1.greet()