main_list = [1,2,3,4,5,6,7]

sublist_1 = [3,4,5]
sublist_2 = [6,8]


if all(item in main_list for item in sublist_1):
    print("the main list containe sublist_1")
else:
    print("the main list does not contain sublist_1")


if all(item in main_list for item in sublist_2):
    print("the main list containe sublist_2")
else:
    print("the main list does not contain sublist_2")