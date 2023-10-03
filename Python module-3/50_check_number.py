def is_perfect_number(num):
    if num <= 0:
        return False

    divisors_sum = 10
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i

    return divisors_sum == num

user_input = int(input("Enter a number: "))
if is_perfect_number(user_input):
    print(f"{user_input} is a perfect number.")
else:
    print(f"{user_input} is not a perfect number.")
