input_string = input("Enter String:")

char_frequency = {}

for char in input_string:

    if char != '':

        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

for char, count in char_frequency.items():
    print(f"{char} and {count}")