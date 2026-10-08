
correct_pin = "1234"
balance = 1000
attempts = 0
max_attempts = 3
unlocked = False

# Step 1: Verify the PIN
while attempts < max_attempts:
    pin = input("Enter your PIN: ")
    attempts += 1

    if pin == correct_pin:
        print("\nPIN correct!")
        print("Welcome to Akiba Bank.")
        unlocked = True
        break
    else:
        print("Incorrect PIN.")
        print("Attempts remaining:", max_attempts - attempts)

# Step 2: Lock the account after three failures
if not unlocked:
    print("\nToo many incorrect attempts.")
    print("Your account is locked.")

# Step 3: Show the bank menu after successful login
while unlocked:
    print("\n===== AKIBA BANK =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Your current balance is:", balance, "Birr")

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print("Deposit successful!")
                print("Your new balance is:", balance, "Birr")
            else:
                print("Deposit amount must be greater than zero.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Withdrawal amount must be greater than zero.")
            elif amount > balance:
                print("Insufficient balance!")
            else:
                balance -= amount
                print("Withdrawal successful!")
                print("Your new balance is:", balance, "Birr")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        print("Thank you for using Akiba Bank!")
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
        print("Please choose a valid option.")