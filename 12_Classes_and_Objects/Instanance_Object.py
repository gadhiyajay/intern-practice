# instance object are the objects that made from class.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def honk(self):
        print("Poom Poom!!")


Volvo = Car("Volvo", "XC90")
BMW = Car("BMW", "M5CS")

print(Volvo.make)
print(Volvo.model)

print(BMW.make)
print(BMW.model)
