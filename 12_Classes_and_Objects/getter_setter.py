class Student:
    def __init__(self, name, age):
        self.newname = name
        self.__private = age  # private variable

    def get_age(self):
        return self.__private

    def set_age(self, age):
        self.__private = age

stud = Student('Jay Gadhiya', 21)

print("Name :", stud.newname, stud.get_age())

stud.set_age(16)

print('Name :', stud.newname, stud.get_age())
