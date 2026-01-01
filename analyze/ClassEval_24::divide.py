@staticmethod
def divide(c1, c2):
    """
        把两个复数相除。
        :param c1: 第一个复数，complex。
        :param c2: 第二个复数，complex。
        :return: 两个复数的商，complex。
        >>> complexCalculator = ComplexCalculator()
        >>> complexCalculator.divide(1+2j, 3+4j)
        (0.44+0.08j)
        """
    denominator = c2.real ** 2 + c2.imag ** 2
    real = (c1.real * c2.real + c1.imag * c2.imag) / denominator
    imaginary = (c1.imag * c2.real - c1.real * c2.imag) / denominator
    return complex(real, imaginary)