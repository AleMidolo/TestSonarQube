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
    if m > n or m < 0 or n < 0:
        return 0
    return math.comb(n, m)