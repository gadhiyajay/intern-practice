try:
    file_location = "sample1.txt"
    contents = input("Enter file contents :")
    with open(file_location, "w") as file:
        file.write(contents)
        print(contents)
        file.close()


except Exception as e:
    print(f"Error : {e}")