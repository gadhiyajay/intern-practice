# program that opens a file and handles a
# FileNotFoundError exception if the file does not exist.

filename = input("Enter the file name you want to open!")
try:
    file = open('filename', "r")
    data = file.read()
    print("The file contents are : ")
    print(data)
    file.close()

except FileNotFoundError:
    print("The file you are looking for was not found!")