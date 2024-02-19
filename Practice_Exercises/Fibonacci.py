def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


x = int(input("Enter the ending numbers! "))
fib(x)
print(fib(x))
