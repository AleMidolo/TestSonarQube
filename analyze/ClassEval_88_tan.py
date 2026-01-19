import math

def tan(self, x):
    """
    Calcola il valore della tangente dell'angolo in gradi x
    :param x: float
    :return: float
    >>> tricalculator.tan(45)
    1.0
    """
    # Converti l'angolo da gradi a radianti
    x_radianti = math.radians(x)
    # Calcola e restituisci la tangente
    return math.tan(x_radianti)