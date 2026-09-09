class Calculator:
    def add(self, a, b):
        print("Addition:", a + b)

    def subtract(self, a, b):
        print("Subtraction:", a - b)

    def multiply(self, a, b):
        print("Multiplication:", a * b)

    def divide(self, a, b):
        print("Division:", a / b)


# Create object
calc = Calculator()

# Call methods
calc.add(10, 5)
calc.subtract(10, 5)
calc.multiply(10, 5)
calc.divide(10, 5)