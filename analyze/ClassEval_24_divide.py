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
    return c1 / c2