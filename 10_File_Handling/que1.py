# function for reading content from a file and displaying it!
# questions link : https://www.pyforschool.com/assignment/file-handling.html
def readfile():
    file = open("poem.txt", "r")
    for line in file:
        print(line, end = "")
    file.close()

readfile()