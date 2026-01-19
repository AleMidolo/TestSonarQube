def count(n, m=None):
    """
    通过从 n 个元素中选择 m 个元素来计算排列的数量（排列）。
    如果未提供 m 或 n 等于 m，则返回 factorial(n)。
    :param n: int，总元素数。
    :param m: int，要选择的元素数（默认=None）。
    :return: int，排列的数量。
    >>> ArrangementCalculator.count(5, 3)
    60

    """
    import math
    
    if m is None or n == m:
        return math.factorial(n)
    
    if m > n or m < 0 or n < 0:
        return 0
    
    # 排列公式: P(n, m) = n! / (n - m)!
    return math.factorial(n) // math.factorial(n - m)