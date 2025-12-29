def sin(self, x):
    """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
    x = x / 180 * pi
    return round(self.taylor_sin(x, 50), 10)