# Palindrome String!
# str = input("Enter a string to check Palindrome :").lower()
# rev_str = str[::-1]
# if str == rev_str:
#     print(f"The entered string {str} is a palindrome string!")
# else:
#     print(f"The entered string {rev_str} is not a palindrome string!")
# THIS WAS WITHOUT THE USE OF FOR LOOP!!
str = input("Enter a string to check Palindrome :").lower()
def pallindrome(num):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str) - i - 1]:
            return False
        return True

if pallindrome(str):
    print("Number is Palindrome!")
else:
    print("Number is NOT Palindrome!")

