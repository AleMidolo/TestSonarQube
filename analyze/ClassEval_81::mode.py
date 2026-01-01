@staticmethod
def mode(data):
    """
        计算给定列表的众数。
        :param data: 给定的列表，list。
        :return: 给定列表的众数，list。
        >>> statistics3 = Statistics3()
        >>> statistics3.mode([1, 2, 3, 3])
        [3]

        """
    from collections import Counter
    if not data:
        return []
    count = Counter(data)
    max_count = max(count.values())
    modes = [key for key, value in count.items() if value == max_count]
    return modes