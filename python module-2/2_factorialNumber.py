num = int(input("Enter Number :"))

factorial = 1

for i in range(1,num + 1):
    factorial *= i

print(f'the factorial {num} is {factorial}')
