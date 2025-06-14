class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0 # ✅ Use the passed value

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount}")
        return True

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew: ${amount}")  # ✅ Fix spelling
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")  # ✅ Proper format
