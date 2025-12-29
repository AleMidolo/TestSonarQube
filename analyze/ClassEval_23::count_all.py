@staticmethod
def count_all(n: int) -> int:
    """
        计算所有可能组合的数量。
        :param n: 元素的总数，int。
        :return: 所有可能组合的数量，int。如果组合数量大于 2^63-1，则返回 float("inf")。
        >>> CombinationCalculator.count_all(4)
        15
        """
    if n < 0:
        return 0
    if n >= 63:
        return float('inf')
    return (1 << n) - 1