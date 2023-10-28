file_name = "my_file.txt"

my_list = ["lenvo","macbook","hp","asus"]

with open(file_name,'w') as file:
    for item in my_list:
        file.write(item + '\n')

    print(f"the lis is writen {file_name}")