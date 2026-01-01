@staticmethod
def count(n: int, m: int) -> int:
    """
        Calcola il numero di combinazioni per un conteggio specifico.
        :param n: Il numero totale di elementi, int.
        :param m: Il numero di elementi in ogni combinazione, int.
        :return: Il numero di combinazioni, int.
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