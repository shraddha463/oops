class Bike:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Color:", self.color)
        print("Price:", self.price)


# Create object
bike1 = Bike("Honda", "Shine", "Black", 85000)

# Display bike details
bike1.display()