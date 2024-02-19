import weakref


class Bear:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Bear {self.name}'

    def get_name(self):
        return 'My name is %s' % self.name


t1 = Bear('Teddy')
print(t1)

ref = weakref.proxy(t1)
print(ref.get_name())

del t1
print(ref.get_name())
