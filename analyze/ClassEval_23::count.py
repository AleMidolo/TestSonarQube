@staticmethod
def count(n: int, m: int) -> int:
    """
        Calcula el número de combinaciones para un conteo específico.
        :param n: El número total de elementos, int.
        :param m: El número de elementos en cada combinación, int.
        :return: El número de combinaciones, int.
        >>> CombinationCalculator.count(4, 2)
        6
        """
    if m < 0 or m > n:
        return 0
    if m > n - m:
        m = n - m
    result = 1
    for i in range(1, m + 1):
        result = result * (n - m + i) // i
    return result