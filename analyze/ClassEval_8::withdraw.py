class BankAccount: 
    def __init__(self, balance=0):
        """
        Initializes a bank account object with an attribute balance, default value is 0.
        """
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits a certain amount into the account, increasing the account balance, return the current account balance.
        If amount is negative, raise a ValueError("Invalid amount").
        :param amount: int
        """
        if amount < 0:
            raise ValueError("Invalid amount")
        self.balance += amount
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
    
    def withdraw(self, amount):
        """
        खाते से एक निश्चित राशि निकालता है, खाते के संतुलन को कम करता है, वर्तमान खाते का संतुलन लौटाता है।
        यदि राशि नकारात्मक है, तो ValueError("अमान्य राशि") उठाएं।
        यदि निकासी राशि खाते के संतुलन से अधिक है, तो ValueError("पर्याप्त संतुलन नहीं है।") उठाएं।
        :param amount: int
        """
        if amount < 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance