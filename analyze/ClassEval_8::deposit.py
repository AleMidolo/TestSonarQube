class BankAccount: 
    def __init__(self, balance=0):
        """
        Initializes a bank account object with an attribute balance, default value is 0.
        """
        self.balance = balance

    def withdraw(self, amount):
        """
        Withdraws a certain amount from the account, decreasing the account balance, return the current account balance.
        If amount is negative, raise a ValueError("Invalid amount").
        If the withdrawal amount is greater than the account balance, raise a ValueError("Insufficient balance.").
        :param amount: int
        """
        if amount < 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance
    
    def view_balance(self):
        """
        Return the account balance.
        """
        return self.balance
    
    def transfer(self, other_account, amount):
        """
        Transfers a certain amount from the current account to another account.
        :param other_account: BankAccount
        :param amount: int
        >>> account1 = BankAccount()
        >>> account2 = BankAccount()
        >>> account1.deposit(1000)
        >>> account1.transfer(account2, 300)
        account1.balance = 700 account2.balance = 300
        """
        self.withdraw(amount)
        other_account.deposit(amount)
    
    def deposit(self, amount):
        """
        खाते में एक निश्चित राशि जमा करता है, खाते के संतुलन को बढ़ाता है, वर्तमान खाते के संतुलन को लौटाता है।
        यदि राशि नकारात्मक है, तो ValueError("अमान्य राशि") उठाएं।
        :param amount: int
        """
        if amount < 0:
            raise ValueError("अमान्य राशि")
        self.balance += amount
        return self.balance