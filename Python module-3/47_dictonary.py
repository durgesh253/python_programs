sample_string = 'w3resource'

char_count = {}

for char in sample_string:
    if char.isalpha(): 
        char = char.lower()  
        char_count[char] = char_count.get(char, 0) + 1

for char, count in char_count.items():
    print(f"'{char}': {count}")
