def tan(self, x):
    """
        x-डिग्री कोण का टैन मान निकालें
        :param x: फ्लोट
        :return: फ्लोट
        >>> tricalculator.tan(45)
        1.0
        """
    if fabs(self.cos(x)) < 1e-10:
        raise ValueError('tan is undefined for angles where cos(x) = 0')
    return round(self.sin(x) / self.cos(x), 10)