@staticmethod
def count_all(n: int) -> int:
    """
        Calculate the number of all possible combinations.
        :param n: The total number of elements,int.
        :return: The number of all possible combinations,int,if the number of combinations is greater than 2^63-1,return float("inf").
        >>> CombinationCalculator.count_all(4)
        15
        """
    total_combinations = (1 << n) - 1
    return total_combinations if total_combinations <= 2 ** 63 - 1 else float('inf')