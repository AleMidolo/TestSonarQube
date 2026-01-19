@staticmethod
def add(c1, c2):
    """
        Aggiunge due numeri complessi.
        :param c1: Il primo numero complesso, complex.
        :param c2: Il secondo numero complesso, complex.
        :return: La somma dei due numeri complessi, complex.
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.add(1+2j, 3+4j)
        (4+6j)

        """
    real = c1.real + c2.real
    imaginary = c1.imag + c2.imag
    return complex(real, imaginary)