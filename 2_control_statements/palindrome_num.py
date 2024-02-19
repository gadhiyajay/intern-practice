# string is read same from both sides
given_string = input("Enter any word to check if it is palindrome : ")
reverse_string = ""
for i in given_string:
    reverse_string = i + reverse_string

if reverse_string == given_string:
    print("The given string", given_string, "is Palindrome")
else:
    print("The given string", given_string, "is NOT Palindrome")
print(reverse_string)