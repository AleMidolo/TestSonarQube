@staticmethod
def count(n, m=None):
    """
        Cuenta el número de arreglos posibles al elegir m elementos de n elementos (permutaciones).
        Si m no se proporciona o n es igual a m, devuelve factorial(n).
        :param n: int, el número total de elementos.
        :param m: int, el número de elementos a elegir (por defecto=None).
        :return: int, el conteo de arreglos.
        >>> ArrangementCalculator.count(5, 3)
        60

        """
    if m is None or n == m:
        return ArrangementCalculator.factorial(n)
    else:
        return ArrangementCalculator.factorial(n) // ArrangementCalculator.factorial(n - m)