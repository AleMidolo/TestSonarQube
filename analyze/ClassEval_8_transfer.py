def transfer(self, other_account, amount):
    """
    Transfiere una cierta cantidad de la cuenta actual a otra cuenta.
    :param other_account: BankAccount
    :param amount: int
    >>> account1 = BankAccount()
    >>> account2 = BankAccount()
    >>> account1.deposit(1000)
    >>> account1.transfer(account2, 300)
    account1.balance = 700 account2.balance = 300
    """
    self.balance -= amount
    other_account.balance += amount
    print(f"account1.balance = {self.balance} account2.balance = {other_account.balance}")