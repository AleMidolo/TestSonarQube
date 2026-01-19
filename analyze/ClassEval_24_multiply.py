@staticmethod
def multiply(c1, c2):
    """
    把两个复数相乘。
    :param c1: 第一个复数，complex。
    :param c2: 第二个复数，complex。
    :return: 两个复数的乘积，complex。
    >>> complexCalculator = ComplexCalculator()
    >>> complexCalculator.multiply(1+2j, 3+4j)
    (-5+10j)

    """
    return c1 * c2