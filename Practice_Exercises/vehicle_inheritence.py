class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def showdetails(self):
        print(f"Vehicle Details : {self.brand} {self.model} {self.year}")

class Car(Vehicle):
    def __init__(self, brand, model, year,seats):
        super().__init__(brand, model, year)
        self.seats = seats

    def showdetails(self):
        super().showdetails()
        print(f"Seats :{self.seats}")

class Bike(Vehicle):
    def __init__(self, brand, model, year,mileage):
        super().__init__(brand, model, year)
        self.mileage = mileage

    def showdetails(self):
        super().showdetails()
        print(f"Mileage :{self.mileage}")

carobj = Car("BMW", "M5CS", 2024, 5)
bikeobj = Bike("Royal Enfield", "Classic", 2015, 35)

carobj.showdetails()
bikeobj.showdetails()
