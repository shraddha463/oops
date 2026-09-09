class Teacher:
    def __init__(self, name, subject, salary):
        self.name = name
        self.subject = subject
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)
        print("Salary:", self.salary)
        print("------------------")


# Create two objects
teacher1 = Teacher("Ramesh", "Python", 30000)
teacher2 = Teacher("Priya", "Data Science", 35000)

# Display details
teacher1.display()
teacher2.display()