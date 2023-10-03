my_tuple = (1,2,3,4,5)

check_element = int(input("Enter Number:"))

if check_element in  my_tuple:
    print(f"{check_element} is in my tuple")
else:
    print(f"{check_element} is not in my tuple")