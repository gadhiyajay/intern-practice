list1 = [12,34,65,12]
list2 = [54,87,56,99]
list3 = [87,45,69,12]

print("3",list3)
list1.extend(list2)
list3.append(list2)
print(list1)
print(id(list1))
print(list3)
print(id(list3))

list4 = list3.copy()
print(" List 4", list4)


x = list3.index(45)
print(x)

list3.insert(2,55)
print(list3)

list3.pop(2)
print("after pop", list3)

list1.remove(34)
print("After remove",list1)
list2.reverse()
print(list2)
list3.sort()
print(list3)

print(list3)

