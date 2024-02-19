size = int(input("Enter size of List"))
list = []
for i  in range(size):
    temp = int(input(f"Enter {i} Index Value :"))
    list.append(temp)
print(list)

def listsum(list):
    if not list:
        return 0
    else:
        return list[0] + listsum(list[1:])

print("Sum of the elements of the list :", listsum(list))