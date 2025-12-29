def transfer(self, other_account, amount):
    """
        Trasferisce una certa somma dal conto corrente a un altro conto.
        :param other_account: BankAccount
        :param amount: int
        >>> account1 = BankAccount()
        >>> account2 = BankAccount()
        >>> account1.deposit(1000)
        >>> account1.transfer(account2, 300)
        account1.balance = 700 account2.balance = 300
        """
    if amount < 0:
        raise ValueError('Invalid amount')
    if amount > self.balance:
        raise ValueError('Insufficient balance.')
    if not isinstance(other_account, BankAccount):
        raise TypeError('other_account must be a BankAccount instance')
    self.balance -= amount
    other_account.balance += amount
    return self.balance