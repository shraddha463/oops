class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def display(self):
        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def calculate_total(self):
        total = self.price * self.quantity
        print("Total Price:", total)

    def apply_discount(self):
        total = self.price * self.quantity
        discount = total * 0.10
        final_price = total - discount
        print("Discount:", discount)
        print("Final Price:", final_price)


# Create object
product1 = Product("Laptop", 50000, 2)

# Call methods
product1.display()
product1.calculate_total()
product1.apply_discount()