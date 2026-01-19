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
    if not data:
        return None
    count_dict = Counter(data)
    max_count = max(count_dict.values())
    modes = [item for item, count in count_dict.items() if count == max_count]
    return modes