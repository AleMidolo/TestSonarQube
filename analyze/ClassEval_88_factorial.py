def factorial(self, a):
    """
    计算 a 的阶乘
    :param a: int
    :return: int
    >>> tricalculator.factorial(5)
    120
    """
    if a < 0:
        raise ValueError("阶乘不支持负数")
    if a == 0 or a == 1:
        return 1
    result = 1
    for i in range(2, a + 1):
        result *= i
    return result