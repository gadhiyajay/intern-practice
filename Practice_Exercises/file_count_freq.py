try:
    file_location = "sample.txt"
    with open(file_location, "r") as file:
        contents = file.read()
        print(contents)
        file.seek(0)
        words = contents.split()
        print(words)
        print(f"No. of words in this file is :{(len(words))}")
        word_count = {}
        for word in set(words):
            word_count[word] = words.count(word)
        for key, value in word_count.items():
            print(key, value)


        file.close()

except FileNotFoundError:
    print("Kyaaa Bhai, esa koi nahi hai yaha!")
except Exception as e:
    print(f"Error : {e}")