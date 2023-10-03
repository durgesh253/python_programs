# What is a list?
# A list in Python is a built-in data structure that represents an ordered collection of items. 
# Lists are versatile and can hold elements of different types, including numbers, strings, and even other lists. 
# Lists are defined using square brackets[ ], and elements within a list are separated by commas.

# my_ list = [1,2,3,4,5]

# To reverse list in python you have few diffrent options:
# 1) using Slicing
my_list = [1,2,3,4,5]
resverse_list = my_list[::-1]
print(resverse_list)

# 2) using reverse() method : 
my_list.reverse()
print(my_list)

# 3) using reversed() function
liste = [1,3,4,5,5]
resverse_list = list(reversed(liste))
print(resverse_list)
