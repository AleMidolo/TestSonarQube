def deposit(self, amount):
    """
    将一定金额存入账户，增加账户余额，返回当前账户余额。
    如果金额为负，则引发 ValueError("Invalid amount")。
    :param amount: int
    """
    if amount < 0:
        raise ValueError("Invalid amount")
    self.balance += amount
    return self.balance