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
    
    # Calculate factorial
    def factorial(num):
        if num <= 1:
            return 1
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
    
    # C(n, m) = n! / (m! * (n - m)!)
    return factorial(n) // (factorial(m) * factorial(n - m))