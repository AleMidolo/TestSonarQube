@staticmethod
def median(data):
    """
        计算给定列表的中位数。
        :param data: 给定的列表，list。
        :return: 给定列表的中位数，float。
        >>> statistics3 = Statistics3()
        >>> statistics3.median([1, 2, 3, 4])
        2.5

        """
    if not data:
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        return float(sorted_data[n // 2])
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2.0