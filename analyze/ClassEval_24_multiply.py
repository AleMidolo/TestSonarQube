@staticmethod
def multiply(c1, c2):
    """
        Multiplica dos números complejos.
        :param c1: El primer número complejo, complejo.
        :param c2: El segundo número complejo, complejo.
        :return: El producto de los dos números complejos, complejo.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.multiply(1+2j, 3+4j)
        (-5+10j)
        """
    real = c1.real * c2.real - c1.imag * c2.imag
    imaginary = c1.real * c2.imag + c1.imag * c2.real
    return complex(real, imaginary)