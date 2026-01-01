def factorial(self, a):
    """
        计算 a 的阶乘
        :param a: int
        :return: int
        >>> tricalculator.factorial(5)
        120
        """
    if a == 0 or a == 1:
        return 1
    else:
        return a * self.factorial(a - 1)