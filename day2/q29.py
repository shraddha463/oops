class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)


# Create object
student1 = Student("Shraddha", 85)

# Display details
student1.display()