class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle("Tesla", 18, 25)
print("The name of the car is :", modelX.name)
print("Max Speed :", modelX.max_speed, "\nMileage :", modelX.mileage)