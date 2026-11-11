class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # Deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(amount, "birr deposited successfully.")
        else:
            print("Deposit amount must be greater than zero.")

    # Withdraw money from the account
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance! Withdrawal denied.")
        else:
            self.balance -= amount
            print(amount, "birr withdrawn successfully.")

    # Display current account balance
    def display_balance(self):
        print("Account Owner:", self.owner)
        print("Current Balance:", self.balance, "birr")
        print("-" * 30)


print("\n========== TASK 5 ==========")

# Create two bank account objects
account1 = BankAccount("Abebe", 1000)
account2 = BankAccount("Hana", 3000)

# Account 1 transactions
print("\nAccount 1 Transactions:")
account1.deposit(500)
account1.withdraw(300)
account1.withdraw(2000)  # This should be rejected
account1.display_balance()

# Account 2 transactions
print("\nAccount 2 Transactions:")
account2.deposit(1000)
account2.withdraw(500)
account2.deposit(200)
account2.withdraw(1000)
account2.display_balance()