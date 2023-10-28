file_name = "my_file.txt"

try:
    with open(file_name,'r') as file:

        file_content = file.read()

        print(file_content)

except FileNotFoundError:
    print(f"the file {file_name} was not found")
except Exception as e:
    print(f"an error occured : {e}")