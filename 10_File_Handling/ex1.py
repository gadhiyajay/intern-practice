import os
f = open('10_File_Handling/title.txt', mode='r', encoding='utf-8')
print("Is file present in the given directory?",os.path.isfile('title.txt'))
print("File name is :", f.name)
print("File encoding is :", f.encoding)
print("Is file closed ?", f.closed)
print("Is the file readable?", f.readable())
print("Is the file writeable?", f.writable())
f.close()
# if we don't close file garbage collector will!, but it's not an efficient way as it
# may be possible that there are many statements after the use of file, and it may corrupt the data!
print("Is the file closed?", f.closed)