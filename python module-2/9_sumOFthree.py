num1 = int(input("Enter num1 :"))
num2 = int(input("Enter num2 :"))
num3 = int(input("Enter num3 :"))

if num1 == num2 or num1 == num3 or num2 == num3:
    result = 0
else:
    result = num1 + num2 + num3

print(f"result is {result}")