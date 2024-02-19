def count_the():
    file = open("title.txt", "r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        if word == "the" or word == "The":
            count += 1
    print("The number of times 'The' appeared is :", count)
    file.close()
count_the()