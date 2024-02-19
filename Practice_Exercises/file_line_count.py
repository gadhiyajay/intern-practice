try:
    file_location = "sample.txt"
    with open(file_location, "r") as file:
        contents = file.read()
        print(contents)
        file.seek(0)
        line_count = 0
        for line in file:
            line_count += 1
        print(f"No. of lines in file is :{line_count}")
        file.close()

except FileNotFoundError:
    print("Kyaaa Bhai, esa koi nahi hai yaha!")
except Exception as e:
    print(f"Error : {e}")