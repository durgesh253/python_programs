
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

keys_to_check = ['a', 'c', 'f', 'e']

for key in keys_to_check:
    print(f"The key '{key}' {'exists' if key in my_dict else 'does not exist'} in the dictionary.")
