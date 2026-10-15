
def record_transaction(history, transaction_type, amount, balance):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "balance_after": balance
    }

    history.append(transaction)


def deposit_money(amount, account):
    if amount <= 0:
        print("Error: Deposit must be greater than zero.")
        return False

    account["balance"] += amount

    record_transaction(
        account["history"],
        "deposit",
        amount,
        account["balance"]
    )

    print(f"Successfully deposited {amount:.2f} Birr.")
    return True


def withdraw_money(amount, account):
    if amount <= 0:
        print("Error: Withdrawal must be greater than zero.")
        return False

    if amount > account["balance"]:
        print("Error: Insufficient balance.")
        return False

    remaining_limit = (
        account["daily_limit"] - account["withdrawn_today"]
    )

    if amount > remaining_limit:
        print(
            f"Error: Daily withdrawal limit exceeded. "
            f"Remaining limit: {remaining_limit:.2f} Birr."
        )
        return False

    account["balance"] -= amount
    account["withdrawn_today"] += amount

    record_transaction(
        account["history"],
        "withdrawal",
        amount,
        account["balance"]
    )

    print(f"Successfully withdrew {amount:.2f} Birr.")
    return True


def check_balance(account):
    return account["balance"]


def generate_transaction_summary(account):
    total_deposited = 0
    total_withdrawn = 0

    for transaction in account["history"]:
        if transaction["type"] == "deposit":
            total_deposited += transaction["amount"]
        elif transaction["type"] == "withdrawal":
            total_withdrawn += transaction["amount"]

    return {
        "opening_balance": account["opening_balance"],
        "total_deposited": total_deposited,
        "total_withdrawn": total_withdrawn,
        "final_balance": account["balance"],
        "transaction_count": len(account["history"]),
        "withdrawn_today": account["withdrawn_today"],
        "remaining_daily_limit": (
            account["daily_limit"] - account["withdrawn_today"]
        )
    }


def display_transaction_history(account):
    print("\n===== TRANSACTION HISTORY =====")

    if len(account["history"]) == 0:
        print("No transactions recorded.")

    for transaction in account["history"]:
        print(
            f"Type: {transaction['type'].title()} | "
            f"Amount: {transaction['amount']:.2f} Birr | "
            f"Balance after: "
            f"{transaction['balance_after']:.2f} Birr"
        )


def display_summary(account):
    summary = generate_transaction_summary(account)

    print("\n===== ACCOUNT SUMMARY =====")
    print(f"Opening balance: {summary['opening_balance']:.2f} Birr")
    print(f"Total deposited: {summary['total_deposited']:.2f} Birr")
    print(f"Total withdrawn: {summary['total_withdrawn']:.2f} Birr")
    print(f"Final balance: {summary['final_balance']:.2f} Birr")
    print(f"Transactions: {summary['transaction_count']}")
    print(f"Withdrawn today: {summary['withdrawn_today']:.2f} Birr")
    print(
        f"Remaining daily limit: "
        f"{summary['remaining_daily_limit']:.2f} Birr"
    )


# Configurable account settings
opening_balance = 1000
daily_withdrawal_limit = 2000

account = {
    "opening_balance": opening_balance,
    "balance": opening_balance,
    "daily_limit": daily_withdrawal_limit,
    "withdrawn_today": 0,
    "history": []
}


# Main program
while True:
    print("\n===== BANKING MENU =====")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Transaction history")
    print("5. Transaction summary")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        try:
            amount = float(input("Enter deposit amount: "))
            deposit_money(amount, account)
        except ValueError:
            print("Error: Enter a valid number.")

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: "))
            withdraw_money(amount, account)
        except ValueError:
            print("Error: Enter a valid number.")

    elif choice == "3":
        print(f"Current balance: {check_balance(account):.2f} Birr")

    elif choice == "4":
        display_transaction_history(account)

    elif choice == "5":
        display_summary(account)

    elif choice == "6":
        print("Thank you for using the banking program.")
        break

    else:
        print("Invalid choice. Please choose from 1 to 6.")
