@staticmethod
def divide(c1, c2):
    """
        Divide dos números complejos.
        :param c1: El primer número complejo, complejo.
        :param c2: El segundo número complejo, complejo.
        :return: El cociente de los dos números complejos, complejo.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.divide(1+2j, 3+4j)
        (0.44+0.08j)
        """
    denominator = c2.real ** 2 + c2.imag ** 2
    real = (c1.real * c2.real + c1.imag * c2.imag) / denominator
    imaginary = (c1.imag * c2.real - c1.real * c2.imag) / denominator
    return complex(real, imaginary)