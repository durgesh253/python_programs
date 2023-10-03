# 43)Why Do You Use the Zip () Method in Python? 
# The zip() function in Python is used to combine multiple iterable objects (such as lists or tuples) 
# element-wise into an iterator.

keys = ['a', 'b', 'c']
values = [1, 2, 3]

my_dict = dict(zip(keys, values))
print(my_dict)