def withdraw(self, amount):
    """
        从账户中提取一定金额，减少账户余额，返回当前账户余额。
        如果金额为负数，抛出 ValueError("Invalid amount")。
        如果提取金额大于账户余额，抛出 ValueError("Insufficient balance.")。
        :param amount: int
        """
    if amount < 0:
        raise ValueError('Invalid amount')
    if amount > self.balance:
        raise ValueError('Insufficient balance.')
    self.balance -= amount
    return self.balance