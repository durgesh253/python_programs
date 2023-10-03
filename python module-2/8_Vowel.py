letter = input("Enter letter : ")

vowels = ['a','e','i','o','u']


if letter.lower() in vowels:
    print(f"{letter} is vowel")
else:
    print(f'{letter} is not a vowel')