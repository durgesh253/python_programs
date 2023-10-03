
# The continue statement in Python is used to skip the rest of the current iteration of a loop
# (for loop or while loop)and move to the next iteration

for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
