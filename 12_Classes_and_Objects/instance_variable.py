class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


s = Dog("Simba")
c = Dog("Casper")
s.add_trick('Roll Over')
c.add_trick('Play Dead')
print(s.tricks)
print(c.tricks)
# class Warehouse:
#     purpose = 'storage'
#     region = 'west'
#
# w1 = Warehouse()
# print(w1.purpose, w1.region)
#
# w2 = Warehouse()
# w2.region = 'east'
# print(w2.purpose, w2.region)

# class Bag:
#     def __init__(self):
#         self.data = []
#
#     def add(self, o):
#         """
#
#         @rtype :
#         """
#         self.data.append(o)
#
#     def addtwice(self, o):
#         self.add(o)
#         self.add(o)
#
# x = 10
# Bag.add(50, x)
# print(x)
