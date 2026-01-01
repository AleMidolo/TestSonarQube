def sin(self, x):
    """
        Calcular el valor del seno del ángulo en grados x
        :param x: float
        :return: float
        >>> tricalculator.sin(30)
        0.5
        """
    x = x / 180 * pi
    return round(self.taylor_sin(x, 50), 10)