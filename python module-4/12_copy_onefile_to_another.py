main_file = 'my_file.txt'
another_file = 'another_file.txt'

with open(main_file , 'r') as main, open(another_file , 'w') as another:
    content = main.read()
    another.write(content)

    print(f"content of {main_file} have been copied to {another_file}")