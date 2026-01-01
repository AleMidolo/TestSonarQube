def count(n: int, m: int) -> int:
    """
    计算特定计数的组合数。
    :param n: 元素的总数，int。
    :param m: 每个组合中的元素数量，int。
    :return: 组合的数量，int。
    >>> CombinationCalculator.count(4, 2)
    6
    """
    if m < 0 or m > n:
        return 0
    if m == 0 or m == n:
        return 1
    numerator = math.factorial(n)
    denominator = math.factorial(m) * math.factorial(n - m)
    return numerator // denominator