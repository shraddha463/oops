class Hotel:
    def __init__(self, name, location, room_type, price):
        self.name = name
        self.location = location
        self.room_type = room_type
        self.price = price

    def display(self):
        print("Hotel Name:", self.name)
        print("Location:", self.location)
        print("Room Type:", self.room_type)
        print("Price:", self.price)


# Create object
hotel1 = Hotel("Taj Hotel", "Mumbai", "Deluxe", 5000)

# Display hotel details
hotel1.display()