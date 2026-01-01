def cos(self, x):
    """
        计算 x 度角的余弦值
        :param x: float
        :return: float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.cos(60)
        0.5
        """
    x = x / 180 * pi
    a = 1
    count = 1
    for k in range(1, 50):
        if count % 2 != 0:
            a -= x ** (2 * k) / self.factorial(2 * k)
        else:
            a += x ** (2 * k) / self.factorial(2 * k)
        count += 1
    return round(a, 10)