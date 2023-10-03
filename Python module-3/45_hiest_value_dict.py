
my_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 40, 'e': 50}

highest_values = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:3]

print("Highest 3 Values in the Dictionary:")
for key, value in highest_values:
    print(f"{key}: {value}")
