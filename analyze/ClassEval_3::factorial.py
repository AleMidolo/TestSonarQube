@staticmethod
def factorial(n):
    """
        Calculates the factorial of a given number.
        :param n: int, the number to calculate the factorial.
        :return: int, the factorial of the given number.
        >>> ArrangementCalculator.factorial(4)
        24
        """
    if n == 0 or n == 1:
        return 1
    return n * ArrangementCalculator.factorial(n - 1)