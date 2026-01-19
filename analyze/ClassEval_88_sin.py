import math

def sin(self, x):
    """
    Calcola il valore del seno dell'angolo di x gradi
    :param x: float
    :return: float
    >>> tricalculator.sin(30)
    0.5
    """
    return math.sin(math.radians(x))