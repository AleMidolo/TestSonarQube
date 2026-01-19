@staticmethod
def subtract(c1, c2):
    """
    Resta dos números complejos.
    :param c1: El primer número complejo, complex.
    :param c2: El segundo número complejo, complex.
    :return: La diferencia de los dos números complejos, complex.
    >>> complexCalculator = ComplexCalculator()
    >>> complexCalculator.subtract(1+2j, 3+4j)
    (-2-2j)

    """
    return c1 - c2