class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)
        print("--------------------")


# Creating 5 employee objects
e1 = Employee("Rahul", 25000, "IT")
e2 = Employee("Priya", 30000, "HR")
e3 = Employee("Amit", 28000, "Sales")
e4 = Employee("Sneha", 35000, "Finance")
e5 = Employee("Ravi", 32000, "IT")

# Display details
e1.display()
e2.display()
e3.display()
e4.display()
e5.display()