def remove_duplicatse(input_list):
# set method is use to remove duplicatse in an array
   new_list = list(set(input_list))
   return new_list




input_list = [1,2,3,1,4,4,5,2]
result_list = remove_duplicatse(input_list)
print("New llist is:", result_list)