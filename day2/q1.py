class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks


# Creating Object
s1 = Student("Shraddha", 21, 85)

# Display Details
print("Name:", s1.name)
print("Age:", s1.age)
print("Marks:", s1.marks)