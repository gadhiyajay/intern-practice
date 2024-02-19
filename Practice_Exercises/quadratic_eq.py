# eq : a x2 + b x + c = 0
import math
def quadratic(a, b, c):
    dis = b**2 - 4*a*c
    print("Discriminant :", dis)
    if dis < 0:
        print("No Real Roots, Only Imaginary Roots!")
    elif dis == 0:
        root = -b/2*a
        print(f"Only One Root Present {root}")
    else:
        posroot = (-b + math.sqrt(dis))/2*a
        negroot = (-b - math.sqrt(dis))/2*a
        print(f"Two Roots present {posroot} and {negroot}")
a = float(input("Enter Value of Coefficient of x2 :"))
b = float(input("Enter Value of Coefficient of x :"))
c = float(input("Enter Value of Constant :"))

quadratic(a, b, c)