class Company:
    def __init__(self, company_name, location, employees):
        self.company_name = company_name
        self.location = location
        self.employees = employees

    def display(self):
        print("Company Name:", self.company_name)
        print("Location:", self.location)
        print("Employees:", self.employees)


# Create object
company1 = Company("Infosys", "Bangalore", 25000)

# Display company details
company1.display()