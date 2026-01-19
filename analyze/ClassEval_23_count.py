@staticmethod
def count(n: int, m: int) -> int:
    """
        计算特定计数的组合数。
        :param n: 元素的总数，int。
        :param m: 每个组合中的元素数量，int。
        :return: 组合的数量，int。
        >>> CombinationCalculator.count(4, 2)
        6
        """
    if m < 0 or m > n:
        return 0
    if m > n // 2:
        m = n - m
    result = 1
    for i in range(1, m + 1):
        result = result * (n - m + i) // i
    return result