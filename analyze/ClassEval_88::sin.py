def sin(self, x):
    """
        Calcola il valore del seno dell'angolo di x gradi
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
    x_rad = x / 180 * pi
    result = 0
    for n in range(50):
        term = (-1) ** n * x_rad ** (2 * n + 1) / self.factorial(2 * n + 1)
        result += term
    return round(result, 10)