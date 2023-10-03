def get_unique_values(input_list):
    unique_set = set(input_list)  
    unique_list = list(unique_set)  
    return unique_list


my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_values = get_unique_values(my_list)
print("Unique Values:", unique_values)
