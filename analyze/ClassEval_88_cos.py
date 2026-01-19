import math

def cos(self, x):
    """
    Calcular el valor del coseno del ángulo en grados x
    :param x: float
    :return: float
    >>> tricalculator = TriCalculator()
    >>> tricalculator.cos(60)
    0.5
    """
    # Convertir grados a radianes
    radianes = math.radians(x)
    # Calcular el coseno
    return math.cos(radianes)