from timeit import timeit


# print(timeit('[n*2 for n in range(100)]', number = 10000))
#
# str1 = """
# num = []
# for n in range(100):
#     num.append(n*2)
#
# """
# print(timeit(str1, number = 10000))

def fact(x):
    fact = 1
    for i in range(1, x + 1):
        fact *= i
    return fact


def rfact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print("Using Loop :", fact(10))
print("Using Recursion :", rfact(10))
import timeit
setup1 = """
from __main__ import fact
x = int(input("Enter the number"))
"""

setup2 = """
from __main__ import rfact
x = int(input("Enter the number"))
"""

print("Perfomance of factorial function with loop :")
print(timeit.timeit(stmt = "fact(x)", setup = setup1, number = 10000))

print("Performance of factorial function with recursion :")
print(timeit.timeit(stmt = "rfact(x)", setup = setup2, number = 10000))