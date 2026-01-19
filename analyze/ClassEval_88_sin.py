def sin(self, x):
    """
    x-डिग्री कोण का sin मान निकालें
    :param x: float
    :return: float
    >>> tricalculator.sin(30)
    0.5
    """
    import math
    return math.sin(math.radians(x))