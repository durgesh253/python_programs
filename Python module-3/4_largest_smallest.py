def get_largest_smallest_sum(numbers):
    if not numbers:
        return None,None,0
    
    largest = smallest = numbers[0]
    total = numbers[0]

    for num in numbers[1:]:
        total += num

        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest , smallest,total

numbers = [12,34,45,2,9,87]
largest, smallest, total = get_largest_smallest_sum(numbers)

print(f"largest Number {largest}")
print(f"Smallest Number {smallest}")
print(f"total Number {total}")