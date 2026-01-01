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
    try:
        if n >= 63:
            result = 2 ** n - 1
            if result > 2 ** 63 - 1:
                return float('inf')
            return int(result)
        else:
            return 2 ** n - 1
    except OverflowError:
        return float('inf')