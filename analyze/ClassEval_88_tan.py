def tan(self, x):
    """
        Calcular el valor de la tangente del ángulo en grados x
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
    return round(self.sin(x) / self.cos(x), 10)