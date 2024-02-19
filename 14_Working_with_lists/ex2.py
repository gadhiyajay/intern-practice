import copy


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name})'


p1 = Person('Cillian')
p2 = Person('Murphy')

L = [p1, p2]
L2 = copy.deepcopy(L)

L[0].name = 'Thomas'

print(L2)

L.append(Person('Shelby'))

print(L2)
print(L2)
