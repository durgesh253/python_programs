while True:
    try:
        user_input = int(input("Enter odd Number : "))
        if user_input % 2 == 0:
            raise ValueError("you entered even number .plzz enter odd number")
        else:
            print(f"you entered odd number {user_input}")
    except ValueError as e:
        print(e)
