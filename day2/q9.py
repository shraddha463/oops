class Movie:
    def __init__(self, name, actor, actress, rating):
        self.name = name
        self.actor = actor
        self.actress = actress
        self.rating = rating

    def display(self):
        print("Movie Name:", self.name)
        print("Actor:", self.actor)
        print("Actress:", self.actress)
        print("Rating:", self.rating)


# Create object
movie1 = Movie("Jawan", "Shah Rukh Khan", "Nayanthara", 8.5)

# Display movie information
movie1.display()