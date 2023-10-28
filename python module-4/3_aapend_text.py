file_name = "my_file.txt"

text_to_append = "Everithing is be all write"

with open(file_name, 'a') as file:
    file.write(text_to_append + '\n')

with open(file_name, 'r') as file:
    file_content = file.read()
    print("Updated file content")
    print(file_content)