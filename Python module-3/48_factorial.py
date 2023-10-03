def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

user_input = int(input("Enter a nonnegative integer: "))

if user_input < 0:
    print("Factorial is undefined for negative numbers.")
else:
    result = factorial_recursive(user_input)
    print(f"The factorial of {user_input} is {result}")
