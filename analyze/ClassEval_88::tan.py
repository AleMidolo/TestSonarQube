def tan(self, x):
    """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
    cos_val = self.cos(x)
    if abs(cos_val) < 1e-10:
        sin_val = self.sin(x)
        if sin_val > 0:
            return float('inf')
        elif sin_val < 0:
            return float('-inf')
        else:
            return 0.0
    sin_val = self.sin(x)
    tan_val = sin_val / cos_val
    return round(tan_val, 10)