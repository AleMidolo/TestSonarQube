def tan(self, x):
    """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
    sin_val = self.sin(x)
    cos_val = self.cos(x)
    if fabs(cos_val) < 1e-10:
        raise ValueError(f'tan({x}) is undefined (cos({x}) = 0)')
    return round(sin_val / cos_val, 10)