input_string = input("Enter String")

if len(input_string ) < 2:
    result = ""
else:
    first_char = input_string[:2]
    last_char = input_string[-2:]

    result = first_char + last_char

print("Result:" , result)