@staticmethod
def factorial(n):
    """
        Calcula el factorial de un número dado.
        :param n: int, el número para calcular el factorial.
        :return: int, el factorial del número dado.
        >>> ArrangementCalculator.factorial(4)
        24

        """
    if n < 0:
        raise ValueError('Factorial is not defined for negative numbers')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result