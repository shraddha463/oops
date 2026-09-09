class Student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks1, self.marks2, self.marks3)

    def calculate_total(self):
        total = self.marks1 + self.marks2 + self.marks3
        print("Total Marks:", total)

    def calculate_percentage(self):
        total = self.marks1 + self.marks2 + self.marks3
        percentage = total / 3
        print("Percentage:", percentage)


# Create object
student1 = Student("Shraddha", 85, 90, 80)

# Call methods
student1.display()
student1.calculate_total()
student1.calculate_percentage()