l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
list1 = l1[1::2]
list2 = l2[0::2]
list1.append(list2)
print(list1)