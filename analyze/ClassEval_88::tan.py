def tan(self, x):
    """
        Calculate the tan value of the x-degree angle
        :param x: float
        :return: float
        >>> tricalculator.tan(45)
        1.0
        """
    if abs(x % 180 - 90) < 1e-10:
        raise ValueError('tan is undefined for 90° + n*180°')
    sin_val = self.sin(x)
    cos_val = self.cos(x)
    if abs(cos_val) < 1e-15:
        raise ValueError('tan is undefined for 90° + n*180°')
    return round(sin_val / cos_val, 10)