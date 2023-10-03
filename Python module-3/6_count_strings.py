def count_strings_with_same_ends(string_list):
    count = 0  # Initialize a counter for matching strings
    
    for s in string_list:
        # Check if the string has a length of 2 or more and the first and last characters are the same
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    
    return count

# Example usage:
string_list = ["aba", "xyz", "level", "aa","bb","sdms" "hello"]
result = count_strings_with_same_ends(string_list)
print("Number of strings with the same first and last character:", result)
