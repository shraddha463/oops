class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        total = self.price * self.quantity
        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total Price:", total)


# Create object
product1 = Product("Laptop", 50000, 2)

# Calculate total price
product1.calculate_total()