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
    
    # Calculate C(n, m) = n! / (m! * (n - m)!)
    # Optimize by using C(n, m) = C(n, n-m) and choosing the smaller value
    m = min(m, n - m)
    
    result = 1
    for i in range(m):
        result = result * (n - i) // (i + 1)
    
    return result