class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


# Creating Object
mobile1 = Mobile("Samsung", "Galaxy S24", 70000)


# Display Mobile Details
print("Brand:", mobile1.brand)
print("Model:", mobile1.model)
print("Price:", mobile1.price)