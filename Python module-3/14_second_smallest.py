my_list = [7    ,3,5,2,4,7]
smallest = second_smallest = float('inf')

for num in my_list:
    if num  < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num
print("Smallest numbers is:", smallest)
print("Second smallest number is:",second_smallest)