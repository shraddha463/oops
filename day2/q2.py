class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department


# Creating Object
e1 = Employee("Shraddha", 30000, "IT")


# Display Details
print("Name:", e1.name)
print("Salary:", e1.salary)
print("Department:", e1.department)