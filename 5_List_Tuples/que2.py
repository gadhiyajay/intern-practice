# Write a program to remove the item present at index 4 and
# add it to the 2nd position and at the end of the list.
list1 = [54, 44, 27, 79, 91, 41]
item = list1.pop(4)
print("The element at 4th index is :", item)
list1.insert(2, item)
list1.append(item)
print(list1)
