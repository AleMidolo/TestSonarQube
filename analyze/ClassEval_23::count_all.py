@staticmethod
def count_all(n: int) -> int:
    """
        Calcola il numero di tutte le possibili combinazioni.
        :param n: Il numero totale di elementi, int.
        :return: Il numero di tutte le possibili combinazioni, int; se il numero di combinazioni è maggiore di 2^63-1, restituisce float("inf").
        >>> CombinationCalculator.count_all(4)
        15
        """
    total = 0
    max_int = 2 ** 63 - 1
    for m in range(1, n + 1):
        comb = CombinationCalculator.count(n, m)
        if total > max_int - comb:
            return float('inf')
        total += comb
    return total