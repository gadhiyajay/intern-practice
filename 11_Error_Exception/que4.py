# prompts the user to input two numbers and
# raises a TypeError exception if the inputs are not numerical.
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
try:
    print(f"The first number is {num1}")
    print(f"The second number is {num2}")
except ValueError:
    print("The values you have entered are not numerical")
except TypeError:
    print("You have entered an invalid type variable!")