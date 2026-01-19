import math

def cos(self, x):
    """
    x-डिग्री कोण का कोस मान निकालें
    :param x:float
    :return:float
    >>> tricalculator = TriCalculator()
    >>> tricalculator.cos(60)
    0.5
    """
    return math.cos(math.radians(x))