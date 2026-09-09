class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print("Car Started")


# Create object
car1 = Car("Toyota", "Innova")

# Call start method
car1.start()