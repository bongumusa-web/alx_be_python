class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = 0 # account balance


    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
        print(f"Deposited: ${amount}")
        return True

    def withdraw(self, amount):
        self.account_balance = self.account_balance - amount
        if self.account_balance > amount :
            print(f"Withderw: ${ amount}")
            return True
        elif self.account_balance < amount :
            print("Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}" )
