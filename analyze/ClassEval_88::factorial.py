def factorial(self, a):
    """
        a का फैक्टोरियल निकालें
        :param a: int
        :return: int
        >>> tricalculator = TriCalculator()
        >>> tricalculator.factorial(5)
        120
        """
    if a < 0:
        raise ValueError('Factorial is not defined for negative numbers')
    result = 1
    for i in range(2, a + 1):
        result *= i
    return result