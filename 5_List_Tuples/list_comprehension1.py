# squares = []
# for i in range(50):
#     squares.append(i**2)
# print(squares)
# list comprehension for the code above would be:
res = [i**2 for i in range(50)]
print("Using list comprehension", res)
# using lambda function
res1 = list(map(lambda x:x**2, range(50)))
print("Using Lambda Function", res1)