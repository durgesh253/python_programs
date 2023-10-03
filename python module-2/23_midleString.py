
main_string = input("Enter the main string: ")


insert_string = input("Enter the string to insert: ")


middle_index = len(main_string) // 2

result_string = main_string[:middle_index] + insert_string + main_string[middle_index:]

print("Result:", result_string)
