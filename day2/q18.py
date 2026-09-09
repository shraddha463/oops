class Restaurant:
    def __init__(self, name, location, rating):
        self.name = name
        self.location = location
        self.rating = rating

    def display(self):
        print("Restaurant Name:", self.name)
        print("Location:", self.location)
        print("Rating:", self.rating)


# Create object
restaurant1 = Restaurant("Spice Garden", "Bangalore", 4.5)

# Display restaurant details
restaurant1.display()