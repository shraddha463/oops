class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Monthly Salary:", self.salary)

    def calculate_annual_salary(self):
        annual_salary = self.salary * 12
        print("Annual Salary:", annual_salary)

    def calculate_bonus(self):
        bonus = self.salary * 0.10
        print("Bonus:", bonus)


# Create object
employee1 = Employee("Rahul", 30000)

# Call methods
employee1.display()
employee1.calculate_annual_salary()
employee1.calculate_bonus()