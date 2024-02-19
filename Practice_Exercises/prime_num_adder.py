# Find Prime numbers and add them till 1000!!
# using for-else statement
def prime(num):
    for i in range (2, num):
        if num % i == 0:
            print("NOT PRIME")
            break
    else:
        print("PRIME!")

num = int(input())
prime(num )