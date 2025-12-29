@staticmethod
def count(n, m=None):
    """
        Counts the number of arrangements by choosing m items from n items (permutations).
        If m is not provided or n equals m, returns factorial(n).
        :param n: int, the total number of items.
        :param m: int, the number of items to be chosen (default=None).
        :return: int, the count of arrangements.
        >>> ArrangementCalculator.count(5, 3)
        60

        """
    if m is None or n == m:
        return ArrangementCalculator.factorial(n)
    if m > n or m < 0:
        return 0
    result = 1
    for i in range(n, n - m, -1):
        result *= i
    return result