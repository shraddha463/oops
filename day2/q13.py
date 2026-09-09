class HospitalPatient:
    def __init__(self, name, age, disease, room_no):
        self.name = name
        self.age = age
        self.disease = disease
        self.room_no = room_no

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Room No:", self.room_no)


# Create object
patient1 = HospitalPatient("Rahul", 25, "Fever", 101)

# Display patient details
patient1.display()