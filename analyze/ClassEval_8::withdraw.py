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
        Preleva un certo importo dal conto, diminuendo il saldo del conto, restituisce il saldo attuale del conto.
        Se l'importo è negativo, solleva un ValueError("Importo non valido").
        Se l'importo del prelievo è maggiore del saldo del conto, solleva un ValueError("Saldo insufficiente.").
        :param amount: int
        """
        if amount < 0:
            raise ValueError("Importo non valido")
        if amount > self.balance:
            raise ValueError("Saldo insufficiente.")
        self.balance -= amount
        return self.balance