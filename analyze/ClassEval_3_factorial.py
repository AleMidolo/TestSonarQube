@staticmethod
def factorial(n):
    """
    Calcola il fattoriale di un numero dato.
    :param n: int, il numero di cui calcolare il fattoriale.
    :return: int, il fattoriale del numero dato.
    >>> ArrangementCalculator.factorial(4)
    24

    """
    if n < 0:
        raise ValueError("Il fattoriale non è definito per numeri negativi")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result