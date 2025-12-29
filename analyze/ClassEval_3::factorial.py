@staticmethod
def factorial(n):
    """
        计算给定数字的阶乘。
        :param n: int，要计算阶乘的数字。
        :return: int，给定数字的阶乘。
        >>> ArrangementCalculator.factorial(4)
        24

        """
    if n < 0:
        raise ValueError('Factorial is not defined for negative numbers')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result