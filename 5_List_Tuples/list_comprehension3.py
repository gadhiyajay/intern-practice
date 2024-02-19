# def print_half_pyramid(rows):
#     for i in range(1, rows + 1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()
#
#
# print_half_pyramid(5)
# from typing import List
# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]
# del list1[3]
# res = list(zip(list1, list2, strict=True))
# print(res)
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11], ]
print("Original Matrix", matrix)
res = list(zip(*matrix))
print(res)
