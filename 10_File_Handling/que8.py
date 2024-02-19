def count_letter():
    file = open("story")
    data = file.read()
    print(data)
    count = 0
    for letter in data:
        if letter.isupper():
            count += 1
    print("The no of upper case letters in the file is :", count)
    file.close()

count_letter()

