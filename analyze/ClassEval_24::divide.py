@staticmethod
def divide(c1, c2):
    """
        Divide due numeri complessi.
        :param c1: Il primo numero complesso, complex.
        :param c2: Il secondo numero complesso, complex.
        :return: Il quoziente dei due numeri complessi, complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.divide(1+2j, 3+4j)
        (0.44+0.08j)

        """
    denominator = c2.real ** 2 + c2.imag ** 2
    if denominator == 0:
        raise ZeroDivisionError('Division by zero complex number')
    real = (c1.real * c2.real + c1.imag * c2.imag) / denominator
    imaginary = (c1.imag * c2.real - c1.real * c2.imag) / denominator
    return complex(real, imaginary)