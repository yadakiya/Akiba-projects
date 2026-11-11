"""Question 2: Encapsulation and access-modifier naming conventions."""


class BankAccount:
    def __init__(self, account_holder, opening_balance=0):
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")

        self.account_holder = account_holder  # Public attribute
        self.__balance = opening_balance      # Name-mangled attribute

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit failed: amount must be greater than zero.")
            return False

        self.__balance += amount
        print(f"Deposit successful. New balance: {self.__balance:.2f}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal failed: amount must be greater than zero.")
            return False

        if amount > self.__balance:
            print("Withdrawal failed: insufficient balance.")
            return False

        self.__balance -= amount
        print(f"Withdrawal successful. New balance: {self.__balance:.2f}")
        return True

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    account = BankAccount("Yadeni Getu", 1000)

    print(f"Account holder: {account.account_holder}")
    print(f"Initial balance: {account.get_balance():.2f}")

    account.deposit(500)
    account.withdraw(200)
    account.withdraw(5000)
    account.deposit(-50)
    account.withdraw(-10)

    print(f"Final balance: {account.get_balance():.2f}")

    # account.__balance = 999999
    # This creates a separate public attribute; it does not change
    # the internally stored _BankAccount__balance.
