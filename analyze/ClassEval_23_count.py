def count(n: int, m: int) -> int:
    """
    Calcula el número de combinaciones para un conteo específico.
    :param n: El número total de elementos, int.
    :param m: El número de elementos en cada combinación, int.
    :return: El número de combinaciones, int.
    >>> CombinationCalculator.count(4, 2)
    6
    """
    if m > n or m < 0 or n < 0:
        return 0
    
    if m == 0 or m == n:
        return 1
    
    # Optimize by using the smaller value (C(n,m) = C(n, n-m))
    m = min(m, n - m)
    
    # Calculate combinations using the formula: n! / (m! * (n-m)!)
    # We calculate it iteratively to avoid overflow with large factorials
    result = 1
    for i in range(m):
        result = result * (n - i) // (i + 1)
    
    return result