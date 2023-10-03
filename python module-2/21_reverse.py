input_string = input("Enter String :")

if len(input_string) % 4 == 0:
    resverse_string = input_string[::-1]
    result = resverse_string
else:
    result = input_string

print("Result" , result)