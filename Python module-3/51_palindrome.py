def is_palindrome(input_str):
    
    cleaned_str = input_str.replace(" ", "").lower()
    
    return cleaned_str == cleaned_str[::-1]

user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
