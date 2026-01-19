@staticmethod
def multiply(c1, c2):
    """
    दो जटिल संख्याओं को गुणा करता है।
    :param c1: पहली जटिल संख्या, complex.
    :param c2: दूसरी जटिल संख्या, complex.
    :return: दो जटिल संख्याओं का गुणनफल, complex.
    >>> complexCalculator = ComplexCalculator()
    >>> complexCalculator.multiply(1+2j, 3+4j)
    (-5+10j)

    """
    return c1 * c2