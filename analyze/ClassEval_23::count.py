def count(n: int, m: int) -> int:
    """
    Calculate the number of combinations for a specific count.
    :param n: The total number of elements,int.
    :param m: The number of elements in each combination,int.
    :return: The number of combinations,int.
    >>> CombinationCalculator.count(4, 2)
    6
    """
    if m < 0 or m > n:
        return 0
    return math.comb(n, m)