tuple_list = [(1,2),(3,4),(5,6)]

new_value = 99

update_tuple_list = [(t[0],new_value) for t in tuple_list]

print("Updated list of tuples:",update_tuple_list)