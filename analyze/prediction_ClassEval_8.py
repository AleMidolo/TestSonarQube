class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self._validate_amount(amount)
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self._validate_amount(amount)
        self._validate_sufficient_balance(amount)
        self.balance -= amount
        return self.balance

    def view_balance(self):
        return self.balance

    def transfer(self, other_account, amount):
        self.withdraw(amount)
        other_account.deposit(amount)

    def _validate_amount(self, amount):
        if amount < 0:
            raise ValueError("Invalid amount")

    def _validate_sufficient_balance(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance.")