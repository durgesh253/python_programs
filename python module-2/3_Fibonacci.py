# Input the range from the user
n = int(input("Enter the range for Fibonacci series: "))

# Initialize the first two Fibonacci numbers
fibonacci_series = [0, 1]

# Generate the Fibonacci series within the given range
while fibonacci_series[-1] + fibonacci_series[-2] <= n:
    next_fibonacci = fibonacci_series[-1] + fibonacci_series[-2]
    fibonacci_series.append(next_fibonacci)

# Print the Fibonacci series
print("Fibonacci series within the given range:")
print(fibonacci_series)
