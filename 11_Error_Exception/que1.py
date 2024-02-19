# ZeroDivisionError if number divided by zero!
dividend = int(input("Enter the number you want to divide!"))
divisor = int(input(f"Enter the number by which you want to divide {dividend} with"))
try:
    # if divisor != 0:
    ans = dividend/divisor
    print(f"The division of the numbers are {ans}")

except Error:
    print("This Division is not allowed!")
