def factorial(self, a):
    """
        Calcular el factorial de a
        :param a: int
        :return: int
        >>> tricalculator.factorial(5)
        120
        """
    if a == 0 or a == 1:
        return 1
    else:
        return a * self.factorial(a - 1)