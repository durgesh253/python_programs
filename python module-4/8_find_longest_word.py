def find_longest_word(text):
    words = text.split()
    longest_word = []
    max_lenght = 0

    for word in words:
        word = word.strip('.,?!;')
        if len(word) > max_lenght:
            max_lenght = len(word)
            longest_word = [word]
        elif len(word) == max_lenght:
            longest_word.append(word)
    
    return longest_word

text = 'This is a simple Python program wonderful to find the longest words in a text. Simple is good.'

longest_words = find_longest_word(text)
if longest_words:
    print("longest word in text:")
    for word in longest_words:
        print(word)
else:
    print("no word found in text")