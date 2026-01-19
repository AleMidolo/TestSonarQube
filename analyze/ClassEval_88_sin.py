def sin(self, x):
    """
    Calculate the sin value of the x-degree angle
    :param x: float
    :return: float
    >>> tricalculator.sin(30)
    0.5
    """
    import math
    return math.sin(math.radians(x))