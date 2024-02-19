num = int(input("Enter an integer"))

reverse_number = 0
while num > 0:
    remainder = num % 10
    reverse_number = (reverse_number * 10) + remainder
    num = num//10
print(reverse_number)


