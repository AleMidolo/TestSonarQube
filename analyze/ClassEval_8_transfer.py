def transfer(self, other_account, amount):
    """
    将一定金额从当前账户转移到另一个账户。
    :param other_account: 银行账户
    :param amount: int
    >>> account1 = BankAccount()
    >>> account2 = BankAccount()
    >>> account1.deposit(1000)
    >>> account1.transfer(account2, 300)
    account1.balance = 700 account2.balance = 300
    """
    if amount <= 0:
        return
    
    if self.balance >= amount:
        self.balance -= amount
        other_account.balance += amount