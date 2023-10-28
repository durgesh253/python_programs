file_name = 'my_file.txt'

with open(file_name, 'r') as file:
    line_count = 0

    for line in file:
        line_count += 1

    print(f"the number of line in the file is : {line_count}")