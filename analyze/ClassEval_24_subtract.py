@staticmethod
def subtract(c1, c2):
    """
    把两个复数相减。
    :param c1: 第一个复数，complex。
    :param c2: 第二个复数，complex。
    :return: 两个复数的差，complex。
    >>> complexCalculator = ComplexCalculator()
    >>> complexCalculator.subtract(1+2j, 3+4j)
    (-2-2j)

    """
    return c1 - c2