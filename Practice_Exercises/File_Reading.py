try:
    file_location = "sample.txt"
    with open(file_location, "r") as file:
        contents = file.read()
        print(contents)
        file.close()

except FileNotFoundError:
    print("Kyaaa Bhai, esa koi nahi hai yaha!")
except Exception as e:
    print(f"Error : {e}")