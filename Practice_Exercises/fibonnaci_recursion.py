# Returns the nth value of the Fibonacci Series!

num = int(input("Enter the Index of Fibonacci Series :"))

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(num))