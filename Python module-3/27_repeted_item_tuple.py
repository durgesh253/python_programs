my_tuple = [1,2,2,3,4,4,5]

repeted_items = [item for item in my_tuple if my_tuple.count(item) > 1]

new_items = list(set(repeted_items))
print(new_items)
