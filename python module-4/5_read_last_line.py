file_name = 'my_file.txt'

n = 5 
with open(file_name, 'r') as file:

    lines = file.readlines()

    last_n_lines = lines[-n:]

    for line in last_n_lines:
        print(line, end='')