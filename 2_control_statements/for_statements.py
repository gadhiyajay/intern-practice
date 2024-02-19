# Take input from the user and sum it up!
num = int(input("Enter the number upto which you want to sum!"))
sum1 = 0
for i in range(1,num+1):
    sum1 = sum1 + i
    print("In loop", i, sum1)
print(sum1)
