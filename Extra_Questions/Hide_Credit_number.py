# Program to hide credit card numbers and display only last 4 digits!
cc_num = input("Enter an valid 12 digit credit card number :")
num_len = len(cc_num)
if num_len < 12 or num_len >= 13:
    print("The entered Credit Card Number is not valid")
else:
    result = "********" + cc_num[-4:num_len]
    print("Result!", result)
