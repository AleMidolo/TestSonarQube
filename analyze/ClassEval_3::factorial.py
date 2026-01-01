@staticmethod
def factorial(n):
    """
        Calcola il fattoriale di un numero dato.
        :param n: int, il numero di cui calcolare il fattoriale.
        :return: int, il fattoriale del numero dato.
        >>> ArrangementCalculator.factorial(4)
        24
        """
    if n == 0 or n == 1:
        return 1
    else:
        return n * ArrangementCalculator.factorial(n - 1)