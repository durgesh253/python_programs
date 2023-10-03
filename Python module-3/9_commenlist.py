def have_common_list():
    for item in list_1:
        if item in list_2:
            return True
    return False


list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9,10]

if have_common_list(list_1,list_2):
    print("the list have at least one common numbar")
else:
    print("The list have do not have any common numbar")    