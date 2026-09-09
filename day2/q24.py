class Mobile:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def call(self):
        print("Calling from", self.brand, self.model)


# Create object
mobile1 = Mobile("Samsung", "Galaxy S24")

# Call method
mobile1.call()