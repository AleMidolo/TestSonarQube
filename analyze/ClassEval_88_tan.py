import math

def tan(self, x):
    """
    Calcular el valor de la tangente del ángulo en grados x
    :param x: float
    :return: float
    >>> tricalculator.tan(45)
    1.0
    """
    # Convertir grados a radianes
    radianes = math.radians(x)
    # Calcular y retornar la tangente
    return math.tan(radianes)