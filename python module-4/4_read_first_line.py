file_name = 'my_file.txt'

n = 5

try:
    with open(file_name, 'r') as file:

        for line_number , line in enumerate(file , 1):
            if line_number <= n:
                print(line, end='')

except FileNotFoundError:
    print(f'file name {file_name} is not found')
except Exception as e:
    print(f'an error occured : {e}')