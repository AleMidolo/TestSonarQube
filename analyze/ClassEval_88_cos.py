def cos(self, x):
    """
        Calcola il valore del coseno dell'angolo in gradi x
        :param x: float
        :return: float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.cos(60)
        0.5
        """
    return self.taylor(x, 50)