def add(c1, c2):
    """
    把两个复数相加。
    :param c1: 第一个复数，complex。
    :param c2: 第二个复数，complex。
    :return: 两个复数的和，complex。
    >>> complexCalculator = ComplexCalculator()
    >>> complexCalculator.add(1+2j, 3+4j)
    (4+6j)

    """
    return complex(c1.real + c2.real, c1.imag + c2.imag)