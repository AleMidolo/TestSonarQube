def cos(self, x):
    """
        Calculate the cos value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.cos(60)
        0.5
        """
    x = x / 180 * pi
    g = 0
    t = 1
    n = 0
    while fabs(t) >= 1e-15:
        g += t
        n += 1
        t = -t * x * x / (2 * n - 1) / (2 * n)
    return round(g, 10)