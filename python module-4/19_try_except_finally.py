try:

    result = 10 / 2
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print("No exception was raised.")
finally:
    print("Cleanup code (always executed).")