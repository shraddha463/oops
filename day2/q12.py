class CollegeStudent:
    def __init__(self, name, roll_no, course, year):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.year = year

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Year:", self.year)


# Create object
student1 = CollegeStudent("Shraddha", 101, "BCA", 3)

# Display student details
student1.display()