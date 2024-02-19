import weakref

class Friend:
    def __init__(self, name):
        self.name = name

alice = Friend("Alice")
bob = Friend("Bob")

alice_weakref = weakref.ref(alice)
bob_weakref = weakref.ref(bob)

print(alice_weakref().name)
print(bob_weakref().name)

alice = None
bob = None

print(alice_weakref())
print(bob_weakref())

6zdrYmP38ETxqAqramMebJXjkU8qTj