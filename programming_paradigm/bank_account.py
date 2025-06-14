class BankAccount:
    def __init__(self,account_balance):
        self.account_balance = 0 # account balance

    def deposit(self, amount):
        self.amount = amount
        self.account_balance += self.amount
        return self.account_balance

    def withdraw(self, amount):
        self.amount = amount
        self.account_balance = self.account_balance - self.amount
        if self.account_balance > self.amount :
            return True
        elif self.account_balance <self.amount :
            return False

    def display_balance(self):
        print(f"Your current balance is: ${self.account_balance:.2f}" )
