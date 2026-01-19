def factorial(self, a):
    """
    Calcular el factorial de a
    :param a: int
    :return: int
    >>> tricalculator.factorial(5)
    120
    """
    if a < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if a == 0 or a == 1:
        return 1
    
    result = 1
    for i in range(2, a + 1):
        result *= i
    return result