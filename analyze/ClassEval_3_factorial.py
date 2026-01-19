@staticmethod
def factorial(n):
    """
        计算给定数字的阶乘。
        :param n: int，要计算阶乘的数字。
        :return: int，给定数字的阶乘。
        >>> ArrangementCalculator.factorial(4)
        24
        """
    if n == 0 or n == 1:
        return 1
    else:
        return n * ArrangementCalculator.factorial(n - 1)