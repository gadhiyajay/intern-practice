def hash_display():
    file = open("poem.txt", "r")
    data = file.read()
    print(data)
    for word in data:
        print(word, end="#")
    file.close()

hash_display()
