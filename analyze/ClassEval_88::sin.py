def sin(self, x):
    """
        Calculate the sin value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
    x_rad = x / 180 * pi
    result = 0
    for n in range(50):
        numerator = x_rad ** (2 * n + 1)
        denominator = self.factorial(2 * n + 1)
        term = numerator / denominator
        if n % 2 == 0:
            result += term
        else:
            result -= term
    return round(result, 10)