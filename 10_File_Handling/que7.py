def count_words():
    file = open("poem.txt", "r")
    count = 0
    data = file.read()
    print(data)
    words = data.split()
    for word in words:
        if word[-1] == 'e':
            count += 1
    print(count)
    file.close()

count_words()