string_1 = input("Enter First String: ")
string_2 = input("Enter Second String: ")


if len(string_1) >=2 and len(string_2) >= 2:

     new_string1 = string_2[:2] + string_1[2:]
     new_string2 = string_1[:2] + string_2[2:]

     result_string = new_string1 + '' + new_string2

print("Result:" , result_string)