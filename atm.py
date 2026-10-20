
balance = 5000
pin = 1234
transactions = []

# Step 1: Verify PIN (maximum 3 attempts)
attempts = 0

while attempts < 3:
    entered_pin = int(input("Enter your ATM PIN: "))

    if entered_pin == pin:
        print("Login successful!")
        break
    else:
        attempts += 1
        print("Incorrect PIN!")

if attempts == 3:
    print("Your account is locked temporarily.")

else:
    # Step 2: ATM Menu
    while True:
        print("\n===== ATM MACHINE =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Available balance:", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                transactions.append(f"Deposited: Rs. {amount:.2f}")
                print("Deposit successful!")
                print("Updated balance:", balance)
            else:
                print("Enter a valid amount.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Enter a valid amount.")
            elif amount <= balance:
                balance -= amount
                transactions.append(f"Withdrawn: Rs. {amount:.2f}")
                print("Please collect your cash.")
                print("Remaining balance:", balance)
            else:
                print("Insufficient balance!")

        elif choice == "4":
            print("\n===== MINI STATEMENT =====")

            if len(transactions) == 0:
                print("No transactions yet.")
            else:
                for transaction in transactions:
                    print(transaction)

            print("Current balance:", balance)

        elif choice == "5":
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid choice!")
