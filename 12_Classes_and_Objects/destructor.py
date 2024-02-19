class Student:
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name
        print('Object Initialized')

    def show(self):
        print('Hello, my name is', self.name)

    # destructor
    def __del__(self):
        print('Inside Destructor')
        print('Object Destroyed')

s1 = Student('Karen')
s1.show()

del s1