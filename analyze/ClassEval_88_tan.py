def tan(self, x):
    """
    x-डिग्री कोण का टैन मान निकालें
    :param x: फ्लोट
    :return: फ्लोट
    >>> tricalculator.tan(45)
    1.0
    """
    import math
    return math.tan(math.radians(x))