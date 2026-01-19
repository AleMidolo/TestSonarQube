def count(n: int, m: int) -> int:
    """
    计算特定计数的组合数。
    :param n: 元素的总数，int。
    :param m: 每个组合中的元素数量，int。
    :return: 组合的数量，int。
    >>> CombinationCalculator.count(4, 2)
    6
    """
    # Handle edge cases
    if m > n or m < 0 or n < 0:
        return 0
    if m == 0 or m == n:
        return 1
    
    # Optimize by using the smaller of m and n-m
    m = min(m, n - m)
    
    # Calculate C(n, m) = n! / (m! * (n-m)!)
    # Using iterative multiplication to avoid overflow with factorials
    result = 1
    for i in range(m):
        result = result * (n - i) // (i + 1)
    
    return result