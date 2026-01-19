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
    if fabs(cos_val) < 1e-15:
        if sin_val > 0:
            return float('inf')
        elif sin_val < 0:
            return float('-inf')
        else:
            return 0.0
    tan_val = sin_val / cos_val
    return round(tan_val, 10)