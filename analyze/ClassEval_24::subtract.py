@staticmethod
def subtract(c1, c2):
    """
        Subtracts two complex numbers.
        :param c1: The first complex number,complex.
        :param c2: The second complex number,complex.
        :return: The difference of the two complex numbers,complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.subtract(1+2j, 3+4j)
        (-2-2j)
        """
    real = c1.real - c2.real
    imaginary = c1.imag - c2.imag
    return complex(real, imaginary)