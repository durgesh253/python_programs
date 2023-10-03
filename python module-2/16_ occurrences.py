while True: 
  sentence = input("Enter sentence :")
  words = sentence.split()
  word_count = {}


  for word in words:
    word = word.strip('.,!?()[]{}"\'').lower()

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

  for  word, count in word_count.items():
    print(f"{word} and {count}")
