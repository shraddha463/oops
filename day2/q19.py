class Flight:
    def __init__(self, flight_no, source, destination, price):
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.price = price

    def display(self):
        print("Flight No:", self.flight_no)
        print("Source:", self.source)
        print("Destination:", self.destination)
        print("Price:", self.price)


# Create object
flight1 = Flight("AI101", "Bangalore", "Delhi", 5500)

# Display flight details
flight1.display()