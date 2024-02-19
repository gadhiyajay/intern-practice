class Book:
    def __init__(self, pages):
        self.pges = pages

    def __add__(self, other):
        if isinstance(other, Book):
            return Book(self.pges ** other.pges)
        else:
            raise ValueError("Unsupported Operand Type : {} {}".format(type(self), type(other)))


b1 = Book(400)
b2 = Book(900)

b3 = (b1 + b2)
print("Total no. of pages are :", b3.pges)