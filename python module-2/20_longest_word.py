def find_longest_word(word_list):
    if not word_list:
        return 0  

    max_length = len(word_list[0])  

    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)  

    return max_length

word_list = ["apple", "banana", "cherry", "date", "elderberry"]
longest_length = find_longest_word(word_list)
print(f"The length of the longest word is {longest_length}.")
