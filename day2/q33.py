class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)


# Create object
student1 = Student("Shraddha")

# Call method
student1.greet()