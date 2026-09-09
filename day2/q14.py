class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print("Price:", self.price)
        print("--------------------")


# Create five laptop objects
laptop1 = Laptop("Dell", "8GB", "512GB", 45000)
laptop2 = Laptop("HP", "16GB", "512GB", 55000)
laptop3 = Laptop("Lenovo", "8GB", "256GB", 40000)
laptop4 = Laptop("Asus", "16GB", "1TB", 65000)
laptop5 = Laptop("Acer", "8GB", "512GB", 42000)

# Display details
laptop1.display()
laptop2.display()
laptop3.display()
laptop4.display()
laptop5.display()