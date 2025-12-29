@staticmethod
def divide(c1, c2):
    """
        Divides two complex numbers.
        :param c1: The first complex number,complex.
        :param c2: The second complex number,complex.
        :return: The quotient of the two complex numbers,complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.divide(1+2j, 3+4j)
        (0.44+0.08j)

        """
    denominator = c2.real ** 2 + c2.imag ** 2
    real = (c1.real * c2.real + c1.imag * c2.imag) / denominator
    imaginary = (c1.imag * c2.real - c1.real * c2.imag) / denominator
    return complex(real, imaginary)