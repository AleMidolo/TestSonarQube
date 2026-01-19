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
    return round(self.taylor(x * 180 / pi, 50), 10)