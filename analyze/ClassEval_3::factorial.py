@staticmethod
def factorial(n):
    """
        Calcula el factorial de un número dado.
        :param n: int, el número para calcular el factorial.
        :return: int, el factorial del número dado.
        >>> ArrangementCalculator.factorial(4)
        24
        """
    if n == 0 or n == 1:
        return 1
    return n * ArrangementCalculator.factorial(n - 1)