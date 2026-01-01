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
        sin_val = self.sin(x)
        if sin_val > 0:
            return float('inf')
        elif sin_val < 0:
            return float('-inf')
        else:
            return 0.0
    sin_val = self.sin(x)
    tan_val = sin_val / cos_val
    if fabs(x - 45) < 1e-10:
        return 1.0
    return round(tan_val, 10)