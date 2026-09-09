class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


# Creating three objects
person1 = Person("Shraddha", 21, "Basavakalyan")
person2 = Person("Rahul", 22, "Bangalore")
person3 = Person("Priya", 20, "Mumbai")


# Display Person 1 details
print("Person 1")
print("Name:", person1.name)
print("Age:", person1.age)
print("City:", person1.city)

print()

# Display Person 2 details
print("Person 2")
print("Name:", person2.name)
print("Age:", person2.age)
print("City:", person2.city)

print()

# Display Person 3 details
print("Person 3")
print("Name:", person3.name)
print("Age:", person3.age)
print("City:", person3.city)