import math

def tan(self, x):
    """
    Calcola il valore della tangente dell'angolo in gradi x
    :param x: float
    :return: float
    >>> tricalculator.tan(45)
    1.0
    """
    return math.tan(math.radians(x))