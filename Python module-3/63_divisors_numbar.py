def sum_of_divisors(number):
    return sum([i for i in range(1, number + 1) if number % i == 0])

num = int(input("Enter a number: "))

result = sum_of_divisors(num)
print(f"The sum of divisors of {num} is {result}.")

