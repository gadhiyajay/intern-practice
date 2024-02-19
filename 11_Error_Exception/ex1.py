# CUSTOM ERRORS
# Without using a class!
custom_error = Exception("Moyee Moyee!")
try:
    raise custom_error
except Exception as ce:
    print(f"Caught an custom exception :{ce}")

# Using a class!
class customerror(Exception):
    def __init__(self, error_message = "This is a custom exception!!"):
        self.error_message = error_message
        super().__init__(self.error_message)

try:
    raise customerror("Moyeeeeeee Moyeeeeeeeeeeeeeeee")
except customerror as ce:
    print(f"Caught a custom exception : {ce}")
class Vehicle:
    def name(self, name):
        return name
#
# v = Vehicle()
# print(v.__class__.__name__)
# class Vehicle:
#     def name(self, name):
#         return name
#
# v = Vehicle()
# print(type(v).__name__)
# print(type(v))
# class Animal:
#     name = ""
#
#     def eat(self):
#         print("I can eat!!")
#
#
# class Dog(Animal):
#     def display(self):
#         print("My name is ", self.name)
#
#
# labrador: Dog = Dog()
#
# labrador.name = "Rohu"
# labrador.display()
# labrador.eat()
