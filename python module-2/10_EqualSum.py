num1 = int(input("Enter first Integer: "))
num2 = int(input("Enter Second Integer: "))


result = (num1 == num2) or (num1 -  num2 == 5) or (num1 + num2 == 5)

if result:
    print('true') 
else:
    print('false')