@staticmethod
def count_all(n):
    """
        计算从 n 个元素中选择至少 1 个元素，至多 n 个元素的所有可能排列的总数。
        :param n: int，总元素数量。
        :return: int，所有排列的数量。
        >>> ArrangementCalculator.count_all(4)
        64

        """
    total_count = 0
    for m in range(1, n + 1):
        total_count += ArrangementCalculator.count(n, m)
    return total_count