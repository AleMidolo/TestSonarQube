@staticmethod
def count_all(n: int) -> int:
    """
        Calcular el número de todas las combinaciones posibles.
        :param n: El número total de elementos, int.
        :return: El número de todas las combinaciones posibles, int; si el número de combinaciones es mayor que 2^63-1, devuelve float("inf").
        >>> CombinationCalculator.count_all(4)
        15
        """
    total_combinations = (1 << n) - 1
    return total_combinations if total_combinations <= 2 ** 63 - 1 else float('inf')