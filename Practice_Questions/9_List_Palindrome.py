def is_palindrome_list(lst):
    return lst == lst[::-1]


nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]

print("Original List :")
print(nums)

print("Check the said list is Palindrome or not?")
print(is_palindrome_list(nums))
colors = ["Red", "Green", "Red"]
print("Original List :")
print(colors)

print("Check the said list is Palindrome or not?")
print(is_palindrome_list(colors))
