num = int(input("Enter the number of which table you want : "))
prod = 1
for i in range(1, 11):
    prod = i * num
    print(num, "*", i, "=", prod)
