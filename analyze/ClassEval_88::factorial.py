def factorial(self, a):
    """
        Calcular el factorial de a
        :param a: int
        :return: int
        >>> tricalculator.factorial(5)
        120
        """
    if a == 0:
        return 1
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result