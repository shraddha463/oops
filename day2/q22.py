class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)


# Create object
employee1 = Employee("Rahul", 30000)

# Call method
employee1.display_salary()