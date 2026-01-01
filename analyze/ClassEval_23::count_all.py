@staticmethod
def count_all(n: int) -> int:
    """
        Calculate the number of all possible combinations.
        :param n: The total number of elements,int.
        :return: The number of all possible combinations,int,if the number of combinations is greater than 2^63-1,return float("inf").
        >>> CombinationCalculator.count_all(4)
        15
        """
    if n < 0:
        return 0
    total = 0
    max_int = 2 ** 63 - 1
    for m in range(1, n + 1):
        comb = CombinationCalculator.count(n, m)
        if total > max_int - comb:
            return float('inf')
        total += comb
    return total