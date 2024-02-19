# There are 2 methods
# 1st!
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


x = int(input("Enter"))
fib(x)

#second method
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
x = int(input("Enter the ending numbers! "))
fib(x)
print(fib(x))
