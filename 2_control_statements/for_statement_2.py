# odd numbers in given range and sum it up
num = int(input("Enter the number upto which you want to sum up : "))
sum1 = 0
for i in range(1, num):
    if i % 2 != 0:
        sum1 = sum1 + i
        print(i, sum1)
