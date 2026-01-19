import math

def cos(self, x):
    """
    Calculate the cos value of the x-degree angle
    :param x:float
    :return:float
    >>> tricalculator = TriCalculator()
    >>> tricalculator.cos(60)
    0.5
    """
    return math.cos(math.radians(x))