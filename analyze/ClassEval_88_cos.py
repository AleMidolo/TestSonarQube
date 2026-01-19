def cos(self, x):
    """
        Calcular el valor del coseno del ángulo en grados x
        :param x: float
        :return: float
        >>> tricalculator = TriCalculator()
        >>> tricalculator.cos(60)
        0.5
        """
    x = x / 180 * pi
    return round(self.taylor(x * 180 / pi, 50), 10)