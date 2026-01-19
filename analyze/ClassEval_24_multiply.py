@staticmethod
def multiply(c1, c2):
    """
    Moltiplica due numeri complessi.
    :param c1: Il primo numero complesso, complex.
    :param c2: Il secondo numero complesso, complex.
    :return: Il prodotto dei due numeri complessi, complex.
    >>> complexCalculator = ComplexCalculator()
    >>> complexCalculator.multiply(1+2j, 3+4j)
    (-5+10j)

    """
    return c1 * c2