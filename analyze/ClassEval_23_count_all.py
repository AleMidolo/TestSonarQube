@staticmethod
def count_all(n: int) -> int:
    """
        Calcola il numero di tutte le possibili combinazioni.
        :param n: Il numero totale di elementi, int.
        :return: Il numero di tutte le possibili combinazioni, int; se il numero di combinazioni è maggiore di 2^63-1, restituisce float("inf").
        >>> CombinationCalculator.count_all(4)
        15
        """
    if n < 0:
        return 0
    total_combinations = (1 << n) - 1
    return total_combinations if total_combinations <= 2 ** 63 - 1 else float('inf')