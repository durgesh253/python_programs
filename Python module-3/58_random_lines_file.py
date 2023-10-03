import random


def read_random_line(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return random.choice(lines).strip()
    except FileNotFoundError:
        return "File not found."

#
filename = '31_dict_tuple.txt'

random_line = read_random_line(filename)
print("Random Line from the File:")
print(random_line)
