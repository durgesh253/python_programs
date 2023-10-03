def is_in_range(number, start, end):
    return start <= number <= end

start_range = 10
end_range = 50

user_input = int(input("Enter a number: "))

if is_in_range(user_input, start_range, end_range):
    print(f"{user_input} is in the range [{start_range}, {end_range}]")
else:
    print(f"{user_input} is not in the range [{start_range}, {end_range}]")
