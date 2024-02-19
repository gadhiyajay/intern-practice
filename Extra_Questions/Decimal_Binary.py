# Program to convert decimal into binary
def decibina(val):
    if val >= 1:
        decibina(val // 2)
    print(val % 2, end="")


num = int(input("Enter the number in Decimal!"))
decibina(num)
