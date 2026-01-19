def sin(self, x):
    """
        计算 x 度角的正弦值
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
    return round(self.cos(90 - x), 10)