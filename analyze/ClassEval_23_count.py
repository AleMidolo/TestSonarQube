@staticmethod
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
    if m > n // 2:
        m = n - m
    result = 1
    for i in range(1, m + 1):
        result = result * (n - i + 1) // i
    return result