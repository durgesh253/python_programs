n = int(input("Enter positive Integer:"))

sum_intiger = 0

if n > 0 :

    for i in range(1, n +1):
        sum_intiger += i
        

    print(f"The sum of first {n} positive intiger is : {sum_intiger}")

else:
    print("Plzzz enter positive intiger")