def sin(self, x):
    """
        x-डिग्री कोण का sin मान निकालें
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
    x = x / 180 * pi
    return round(self.taylor_sin(x, 50), 10)