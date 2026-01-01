def taylor(self, x, n):
    """
        Trova il valore dell'espansione di Taylor di n-esimo ordine di cos (x/180 * pi)
        :param x: int
        :param n: int
        :return: float
        >>> tricalculator.taylor(60, 50)
        0.5000000000000001
        """
    x = x / 180 * pi
    cos_value = 0
    for i in range(n):
        cos_value += (-1) ** i * x ** (2 * i) / self.factorial(2 * i)
    return cos_value