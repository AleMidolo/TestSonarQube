def tan(self, x):
    """
        Calcola il valore della tangente dell'angolo in gradi x
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
    sin_val = self.sin(x)
    cos_val = self.cos(x)
    if fabs(cos_val) < 1e-10:
        if sin_val > 0:
            return float('inf')
        else:
            return float('-inf')
    return round(sin_val / cos_val, 10)