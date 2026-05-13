# File handling
# Opening a file
# open(file_name, mode_to_open)
# modes: r(read),x(create),w(write),a(append),t(text),b => r,t are default modes

# file_handler = open("Practice.txt", "rt")
# print(file_handler)
# # read file
# print(file_handler.read())
#
# # Close a file
# file_handler.close()
print("#################################")
# fh = open("file1.txt", "xt") # already ran this program and file is created so we can't run again as the file already exists
# # write into file => write(content)
# fh.write("This file is created in python using x mode.\n")
# fh.write("Next line.")
# fh.close()
# reading the created files
fh = open("file1.txt", "rt")
print(fh.read())
fh.close()
print("###################################")
# fh = open("file2.txt", "xt") # file 2 is created and can't create same file
# # write into file => write(content)
# fh.write("This file is created in python using x mode.\n")
# fh.write("Next line.")
# fh.close()
# overwrite a file
# fh = open("file2.txt", "wt")
# fh.write("This file is overwritten using 'w' mode in python \n")
# fh.write("have a nice day!")
# fh.close()
# if file doesn't exist it will create a file in w mode where file3.txt doesn't exist
fh = open("file3.txt", "wt")
fh.write("This file is overwritten using 'w' mode in python \n")
fh.write("Good morning, how is your day\n")
fh.write("Welcome to learning pyhton\n")
fh.write("File handling in python\n")
fh.write("have a nice day")
fh.close()

# Read operation
# read() => reads the content in the file as string
file_handler = open("Practice.txt", "rt")
content = file_handler.read(20) # it reads 1st 20 characters of file
file_handler.close()
print(content)
print(type(content))
print("#############################")
# read line
fh = open("file2.txt", "rt")
line1 = fh.readline()
line2 = fh.readline()
print(f"line1: {line1}")
print(f"line2: {line2}")
fh.close()
print("#############################")
# readlines
fh2 = open("file3.txt", "rt")
lines = fh2.readlines()
fh2.close()
print(f"Lines: {lines}") # gives a list with each line as an element
print("#############################")
# print each line
for line in lines:
    print(line.rstrip('\n')) # to remove space btwn each line we use rstrip to remove\n from right side of the str
print("#############################")

# a mode append, if file doesn't exist a new file will be created
fh3 = open("file3.txt", "at")
fh3.write("\nThis content is appended to the end of the file using 'a' mode in python\n")
fh3.write("Good bye!!")
fh3.close()
fh3 = open("file3.txt", "rt")
print(fh3.read())
print("#############################")
fh4 = open("file4.txt", "at")
fh4.write("This content is created using 'a' mode in python\n")
fh4.write("Good bye!!")
fh4.close()
fh4 = open("file4.txt", "rt")
print(fh4.read())
print("#############################")
fh1 = open("Practice.txt", "rt")
contents = fh1.readlines()
fh1.close()
print(contents)
print("#############################")
# using with statement and automation file closure
with open("Practice.txt", "rt") as fh:
    contents = fh.read()

print(contents) # print outside the with hence file automatically closes
print("#############################")
# with open("practice2.txt", "xt") as file_h:
#     file_h.write("New file is created\n")
#     file_h.write("Good bye")

file_contents = open("practice2.txt", "rt")
print(file_contents.read())
print("#############################")
# Check files exists import os module
# os.path.exists()
import os
# with file name
file_name = "practice2.txt"
if os.path.exists(file_name):
    print("file exists")
else:
    print("file does not exist")
print("#############################")
# with absolute path
# C:\Users\surya\PycharmProjects\PythonProject\src\ex_020326\practice2.txt change the backslash to forward slash as python use backslash other operations
file_name = "C:/Users/surya/PycharmProjects/PythonProject/src/ex_020326/practice2.txt"
if os.path.exists(file_name):
    print("file exists")
else:
    print("file does not exist")
print("#############################")
# using pathlib.path.exists()
from pathlib import Path
file_name = Path("C:/Users/surya/PycharmProjects/PythonProject/src/ex_020326/practice2.txt")
if file_name.exists():
    print("file exists: cannot create a file")
else:
    print("file does not exist: creating file")
    fh5 = open(file_name, "xt")
    fh5.write("creating a file with some contents")
    fh5.close()