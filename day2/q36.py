class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_price(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)


# Create object
mobile1 = Mobile("Samsung", "Galaxy S24", 60000)

# Display price
mobile1.display_price()