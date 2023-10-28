file_name = 'my_file.txt'

with open(file_name,'r') as file:

    file_content = ''

    for line in file:
        file_content += line

        print(file_content)