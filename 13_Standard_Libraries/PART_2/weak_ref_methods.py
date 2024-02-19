import weakref
import gc


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hello, my name is {self.name}!')


def callback_func(ref):
    print("Referenced object is about to be garbage collected")


person = Person("ALICE")
weak_ref = weakref.ref(person, callback_func)

if weak_ref is not None:
    weak_ref().greet()

proxy = weakref.proxy(person)
proxy.greet()

gc.collect()

if weak_ref() is None:
    print("Object has been garbage collected")

try:
    proxy.greet()
except ReferenceError:
    print("Proxy object has been invalidated!!")

weak_dict = weakref.WeakValueDictionary()
weak_dict["key"] = weakref.ref(person)

value = weak_dict.get("key")
print(value)


def finalize_func(obj):
    print(f"Finalizing object : {obj}")


finalize = weakref.finalize(person, finalize_func)
finalize.atexit = True

person = None

gc.collect()
