# program that prompts the user to input an integer and
# raises a ValueError exception if the input is not a valid integer.
num = int(input("Enter an valid integer value! "))
try:
        print(f"The entered number is {num}")
except ValueError:
    print("The entered value is not a valid integer!")