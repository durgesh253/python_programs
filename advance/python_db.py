import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pharmacy_db"
)

cursor = mydb.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS managers( id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL);")
cursor.execute("CREATE TABLE IF NOT EXISTS medicines( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, quantity INT NOT NULL, price INT NOT NULL);")


def RegisterUser(user_type):
    username = input("Enter Username:")
    password = input("Enter Password:")

    if user_type == "admin":
        cursor.execute(
            "INSERT INTO managers (username, password) VALUES (%s, %s)", (username, password))
    elif user_type == "manager":
        cursor.execute("INSERT INTO managers (username, password) VALUES (%s, %s)",
                       (username, password))

    mydb.commit()
    print(f"{user_type.capitalize()} Registered Successfully")


def LoginUser(user_type):
    username = input("Enter Username:")
    password = input("Enter Password:")

    cursor.execute(
        "SELECT * FROM managers WHERE username = %s and password = %s", (username, password))
    result = cursor.fetchall()

    if result:
        print(f"{user_type} Logged Successfully")
    else:
        print("Invalid user. Please try again")


def Add_medicines():
    name = input("Enter Medicine name:")
    quantity = input("Enter Quantity:")
    price = input("Enter Price:")

    cursor.execute(
        "INSERT INTO medicines (name, quantity, price) VALUES (%s, %s, %s)", (name, quantity, price))
    mydb.commit()
    print("Medicine Added Successfully!")


def View_medicines():
    cursor.execute("SELECT * FROM medicines")
    medicines = cursor.fetchall()

    if medicines:
        print("Medicines List:")
        for medicine in medicines:
            print(
                f"Id:{medicine[0]}, Name:{medicine[1]}, Quantity:{medicine[2]}, Price:{medicine[3]}")
    else:
        print("No medicines available")


def Delete_medicine():
    medicine_id = input("Enter Medicine Id To Delete Medicine:")

    cursor.execute("DELETE FROM medicines WHERE id = %s", (medicine_id,))
    mydb.commit()
    print("Medicine Deleted Successfully")


def main():
    print("Welcome to the pharmacy management system")

    while True:
        print("\nSelect User Type:")
        print("1. Admin")
        print("2. Pharmacy Manager")
        print("3. Exit")

        choice = input("Enter Your Choice(1/2/3):")

        if choice == "1":

            print("\nAdmin Operations:")
            print("1. Register User:")
            print("2. Login User:")
            print("3. View All Managers:")
            print("4. View All Medicines:")
            print("5. Exit")

            admin_choice = input("Enter your choice(1/2/3/4/5): ")

            if admin_choice == "1":
                RegisterUser('admin')
            elif admin_choice == "2":
                LoginUser('admin')
            elif admin_choice == "3":
                cursor.execute("SELECT * FROM managers")
                managers = cursor.fetchall()

                if managers:
                    print("\nManagers List:")
                    for manager in managers:
                        print(
                            f"ID:{manager[0]}, Username:{manager[1]}, Pharmacy Name:{manager[2]}")
                else:
                    print("No Managers Available")
            elif admin_choice == "4":
                View_medicines()
            elif admin_choice == "5":
                break
            else:
                print("Invalid Choice. Please Try Again Later")

        elif choice == "2":
            print("\nManager Operation:")
            print("1. Register User:")
            print("2. Login User:")
            print("3. View All Medicines:")
            print("4. Add Medicines:")
            print("5. Delete Medicine")
            print("6. Exit")

            manager_choice = input("Enter your choice(1/2/3/4/5/6): ")

            if manager_choice == "1":
                RegisterUser('manager')
            elif manager_choice == "2":
                LoginUser('manager')
            elif manager_choice == "3":
                View_medicines()
            elif manager_choice == "4":
                Add_medicines()
            elif manager_choice == "5":
                Delete_medicine()
            elif manager_choice == "6":
                break
            else:
                print("Invalid Choice. Please Try Again Later")

        elif choice == "3":
            print("Exit Pharmacy Management System. Goodbye!")
            break

        else:
            print("Invalid Choice")

    mydb.close()


if __name__ == "__main__":
    main()
