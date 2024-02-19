# Count the Vowels in the string!
str1 = input("Enter any string!")
count = 0
vowels = "AEIOUaeiou"
for i in str1:
    if i in vowels:
        count += 1
print("No. of Vowels in the given string is :", count)
