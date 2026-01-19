def transfer(self, other_account, amount):
    """
    वर्तमान खाते से दूसरे खाते में एक निश्चित राशि स्थानांतरित करता है।
    :param other_account: BankAccount
    :param amount: int
    >>> account1 = BankAccount()
    >>> account2 = BankAccount()
    >>> account1.deposit(1000)
    >>> account1.transfer(account2, 300)
    account1.balance = 700 account2.balance = 300
    """
    if self.balance >= amount:
        self.balance -= amount
        other_account.balance += amount