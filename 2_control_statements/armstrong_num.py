num = int(input("Input the number to check if it is armstrong"))
print("Entered number is : ", num)

num = str(num)
len_of_num = len(num)

sum1 = 0
for i in num:
    sum1 = sum1 + int(i)**len_of_num
print(sum1)
if sum1 == int(num):
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")
