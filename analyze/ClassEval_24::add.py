@staticmethod
def add(c1, c2):
    """
        Suma dos números complejos.
        :param c1: El primer número complejo, complejo.
        :param c2: El segundo número complejo, complejo.
        :return: La suma de los dos números complejos, complejo.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.add(1+2j, 3+4j)
        (4+6j)

        """
    real = c1.real + c2.real
    imaginary = c1.imag + c2.imag
    return complex(real, imaginary)