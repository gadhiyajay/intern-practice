import time
start_time = time.time()
class Dog:
    def speak(self):
        return "Woof!!!"

class Duck:
    def speak(self):
        return "Quack Quack"

class Airplane:
    def fly(self):
        return "Fly with Fuel"
def animal_sound(animal):
    return animal.speak()

dog = Dog()
duck = Duck()

print(animal_sound(dog),"\n",animal_sound(duck))


end_time = time.time()
Total_time = end_time - start_time
print("Starting Time of the program was :", start_time)
print("Ending Time of the program is :", end_time)
print("Total time elapsed is :", Total_time)