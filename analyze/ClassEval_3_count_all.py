@staticmethod
def count_all(n):
    """
    Counts the total number of all possible arrangements by choosing at least 1 item and at most n items from n items.
    :param n: int, the total number of items.
    :return: int, the count of all arrangements.
    >>> ArrangementCalculator.count_all(4)
    64

    """
    import math
    
    total = 0
    # For each possible number of items to choose (from 1 to n)
    for k in range(1, n + 1):
        # Calculate the number of arrangements: P(n, k) = n! / (n-k)!
        arrangements = math.factorial(n) // math.factorial(n - k)
        total += arrangements
    
    return total