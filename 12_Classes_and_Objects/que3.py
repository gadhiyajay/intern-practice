class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_Bus = Bus("School Volvo", 180, 12)
print("Vehicle Name :", School_Bus.name, "\nMax_speed :", School_Bus.max_speed, "\nMileage :", School_Bus.mileage)
