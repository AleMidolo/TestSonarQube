def factorial(self, a):
    """
        Calculate the factorial of a
        :param a: int
        :return: int
        >>> tricalculator.factorial(5)
        120
        """
    if a == 0 or a == 1:
        return 1
    else:
        return a * self.factorial(a - 1)