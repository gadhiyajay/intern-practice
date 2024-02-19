str = "Jay gaDhiya"
upper_count = 0
lower_count = 0
for i in str:
    # temp = i
    if i.isupper():
        upper_count += 1
    else:
        lower_count += 1
print("The number of Upper Case words are :", upper_count)
print("The number of Lower Case words are :", lower_count)
