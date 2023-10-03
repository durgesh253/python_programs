# If you want to pick a random item from a range of integers, you can use the random.choice()
#  function along with the range() function

import random


my_range = range(1, 11)  

random_item = random.choice(my_range)

print("Random Item from the Range:", random_item)
