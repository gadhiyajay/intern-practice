# Create a list by picking an odd-index items
# from the first list and even index items from the second
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

# l3 = []
# l4 = []
# for i in l1[1::2]:
#     l3.append(i)
# for j in l2[0::2]:
#     l4.append(j)
# print("List with odd index numbers are :",l3)
# print("List with even index numbers are :",l4)
def double(x):
    return x * x


l3 = list(map(double, l1))
print(l3)
