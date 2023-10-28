from collections import Counter

file_name = "my_file.txt"

try:
    with open(file_name , 'r') as file:
        file_content = file.read()

        words = file_content.lower().split()

        word_count = Counter(words)

        for word , count in word_count.items():
            print(f"{word} : {count}")

except  FileNotFoundError:
    print(f"the file {file_name} is not found")
except Exception as e:
    print(f"an error occured: {e}")
