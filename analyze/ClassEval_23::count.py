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
    if m == 0 or m == n:
        return 1
    numerator = math.factorial(n)
    denominator = math.factorial(m) * math.factorial(n - m)
    return numerator // denominator