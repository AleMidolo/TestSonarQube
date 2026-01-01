@staticmethod
def divide(c1, c2):
    """
        दो जटिल संख्याओं को विभाजित करता है।
        :param c1: पहली जटिल संख्या, complex.
        :param c2: दूसरी जटिल संख्या, complex.
        :return: दो जटिल संख्याओं का भागफल, complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.divide(1+2j, 3+4j)
        (0.44+0.08j)

        """
    denominator = c2.real ** 2 + c2.imag ** 2
    if denominator == 0:
        raise ZeroDivisionError('Cannot divide by zero complex number')
    real = (c1.real * c2.real + c1.imag * c2.imag) / denominator
    imaginary = (c1.imag * c2.real - c1.real * c2.imag) / denominator
    return complex(real, imaginary)