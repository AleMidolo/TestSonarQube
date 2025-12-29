@staticmethod
def subtract(c1, c2):
    """
        दो जटिल संख्याओं को घटाता है।
        :param c1: पहली जटिल संख्या, complex.
        :param c2: दूसरी जटिल संख्या, complex.
        :return: दो जटिल संख्याओं का अंतर, complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.subtract(1+2j, 3+4j)
        (-2-2j)

        """
    real = c1.real - c2.real
    imaginary = c1.imag - c2.imag
    return complex(real, imaginary)