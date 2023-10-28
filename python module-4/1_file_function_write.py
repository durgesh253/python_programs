
# 1)What is File function in python? What is keywords to create and write file. 
# In Python, the open() function is used to work with files.
# The open() function is a built-in function that allows you to open files for various operations, such as reading, writing, or appending data.
# It returns a file object that can be used to perform operations on the file.

# syntax =
# file = open(filename , mode)

with open('my_file.txt' , 'w') as file:
    file.write("hello Durgesh\n")
    file.write("welcome to my youtube channel")