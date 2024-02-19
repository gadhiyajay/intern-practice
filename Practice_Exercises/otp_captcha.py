import random
import string

letters = string.digits + string.ascii_letters
temp = []
for i in range(4):
    x = random.choice(letters)
    temp.append(x)
otp = "".join(temp)
print(f"Your Random OTP is : {otp}")