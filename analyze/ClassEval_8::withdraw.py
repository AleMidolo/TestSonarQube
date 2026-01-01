def withdraw(self, amount):
    """
        Withdraws a certain amount from the account, decreasing the account balance, returns the current account balance.
        If amount is negative, raise ValueError("Invalid amount").
        If withdrawal amount exceeds account balance, raise ValueError("Insufficient balance.").
        :param amount: int
        """
    if amount < 0:
        raise ValueError('Invalid amount')
    if amount > self.balance:
        raise ValueError('Insufficient balance.')
    self.balance -= amount
    return self.balance