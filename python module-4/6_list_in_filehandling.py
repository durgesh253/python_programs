file_name = 'my_file.txt'

with open(file_name, 'r') as file:

    lines = []

    for line in file:
        lines.append(line)

    for line in lines:
        print(line,end='')