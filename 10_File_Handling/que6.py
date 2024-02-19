def count_words():
    file = open("poem.txt", "r")
    count = 0
    data = file.read()
    print(data)
    words = data.split()
    breakpoint()
    for word in words:
        if word == "this" or word =="these":
            count += 1
    print("No of times 'this' or 'these' occured in this file is :", count)
    file.close()

count_words()