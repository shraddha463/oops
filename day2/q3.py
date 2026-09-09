class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


# Creating first object
car1 = Car("BMW", "X5", 8000000)

# Creating second object
car2 = Car("Audi", "A4", 5000000)


# Display first car details
print("Car 1 Details")
print("Brand:", car1.brand)
print("Model:", car1.model)
print("Price:", car1.price)


print()


# Display second car details
print("Car 2 Details")
print("Brand:", car2.brand)
print("Model:", car2.model)
print("Price:", car2.price)