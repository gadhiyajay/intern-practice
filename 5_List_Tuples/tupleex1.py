tuple1 = (10, 20, 30, 40, 50)
list1 = []
for i in tuple1[::-1]:
    list1.append(i)

res = tuple(list1)
print(res)