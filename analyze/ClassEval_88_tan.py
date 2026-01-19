def tan(self, x):
    """
        x-डिग्री कोण का टैन मान निकालें
        :param x: फ्लोट
        :return: फ्लोट
        >>> tricalculator.tan(45)
        1.0
        """
    cos_val = self.cos(x)
    if fabs(cos_val) < 1e-10:
        raise ValueError(f'tan({x}) is undefined (cos({x}) = 0)')
    sin_val = self.sin(x)
    return round(sin_val / cos_val, 10)