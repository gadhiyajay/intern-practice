from collections import OrderedDict


def remove_duplicates(lst):
    return list(OrderedDict.fromkeys(lst))


nums = [1, 2, 4, 3, 5, 4, 6, 9, 2, 1]

print("Original List :")
print(nums)

result = remove_duplicates(nums)

print("Remove Duplicates from the said list while preserving the order :")
print(result)

chars = ['a', 'a', 'b', 'a', 'a', 'c', 'c', 'c', 'd', 'e', 'a', 'b', 'b', 'b']

print("Original List :")
print(chars)

result = remove_duplicates(chars)

print("Remove Duplicates from the said list while preserving the order :")
print(result)