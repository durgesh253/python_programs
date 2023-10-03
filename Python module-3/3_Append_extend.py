# Append() => this method is used to add a single element to the end of list.

my_list = [1,2,3]
my_list.append(4)
print("Updated list :", my_list)

# Extend() => This method is used to append multiple elements from an iterable (e.g., another list) to the end of an existing list.

my_list1 = [1,2,3]
my_list2 = [4,5,6]
my_list1.extend(my_list2)
print("Adding List id",my_list1)