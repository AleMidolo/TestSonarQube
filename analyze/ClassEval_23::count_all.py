@staticmethod
def count_all(n: int) -> int:
    """
        Calcular el número de todas las combinaciones posibles.
        :param n: El número total de elementos, int.
        :return: El número de todas las combinaciones posibles, int; si el número de combinaciones es mayor que 2^63-1, devuelve float("inf").
        >>> CombinationCalculator.count_all(4)
        15
        """
    if n < 0:
        return 0
    if n >= 63:
        total = 2 ** n - 1
        if total > 2 ** 63 - 1:
            return float('inf')
    return 2 ** n - 1