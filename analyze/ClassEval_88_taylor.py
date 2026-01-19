def taylor(self, x, n):
    """
        计算 cos (x/180 * pi) 的 n 阶泰勒展开值
        :param x: int
        :param n: int
        :return: float
        >>> tricalculator.taylor(60, 50)
        0.5000000000000001
        """
    x = x / 180 * pi
    result = 0
    for i in range(n):
        result += (-1) ** i * x ** (2 * i) / self.factorial(2 * i)
    return result