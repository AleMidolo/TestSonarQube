def taylor(self, x, n):
    """
        计算 cos (x/180 * pi) 的 n 阶泰勒展开值
        :param x: int
        :param n: int
        :return: float
        >>> tricalculator.taylor(60, 50)
        0.5000000000000001
        """
    x_rad = x / 180 * pi
    result = 0
    for i in range(n):
        term = (-1) ** i * x_rad ** (2 * i) / self.factorial(2 * i)
        result += term
    return result