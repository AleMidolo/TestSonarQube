def sin(self, x):
    """
        Calcola il valore del seno dell'angolo di x gradi
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
    x = x / 180 * pi
    a = x
    count = 1
    for k in range(1, 50):
        if count % 2 != 0:
            a -= x ** (2 * k + 1) / self.factorial(2 * k + 1)
        else:
            a += x ** (2 * k + 1) / self.factorial(2 * k + 1)
        count += 1
    return round(a, 10)