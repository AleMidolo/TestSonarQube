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
    total = 0
    max_int = 2 ** 63 - 1
    for m in range(1, n + 1):
        comb = CombinationCalculator.count(n, m)
        if total > max_int - comb:
            return float('inf')
        total += comb
    return total