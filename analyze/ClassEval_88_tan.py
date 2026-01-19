def tan(self, x):
    """
        x-डिग्री कोण का टैन मान निकालें
        :param x: फ्लोट
        :return: फ्लोट
        >>> tricalculator.tan(45)
        1.0
        """
    cos_val = self.cos(x)
    if abs(cos_val) < 1e-10:
        return float('inf') if self.sin(x) > 0 else float('-inf')
    sin_val = self.sin(x)
    return round(sin_val / cos_val, 10)