tuple_list = [(1,"A"),(2,"B"),(3,"C")]

numbers,letters = zip(*tuple_list)

print("Numbers",numbers)
print("Letters",letters)