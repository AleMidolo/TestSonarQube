@staticmethod
def factorial(n):
    """
        Calculates the factorial of a given number.
        :param n: int, the number to calculate the factorial.
        :return: int, the factorial of the given number.
        >>> ArrangementCalculator.factorial(4)
        24

        """
    if n < 0:
        raise ValueError('Factorial is not defined for negative numbers')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result