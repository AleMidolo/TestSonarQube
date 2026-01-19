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
    if m == 0 or m == n:
        return 1
    
    # Calculate C(n, m) = n! / (m! * (n-m)!)
    # Optimize by using C(n, m) = C(n, n-m) and choosing the smaller value
    m = min(m, n - m)
    
    result = 1
    for i in range(m):
        result = result * (n - i) // (i + 1)
    
    return result