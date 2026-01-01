@staticmethod
def standard_deviation(data):
    """
        计算给定列表的标准差。
        :param data: 给定的列表，list。
        :return: 给定列表的标准差，float。
        >>> statistics3 = Statistics3()
        >>> statistics3.standard_deviation([1, 2, 3])
        1.0

        """
    if len(data) == 0:
        return None
    mean = Statistics3.mean(data)
    variance = sum(((x - mean) ** 2 for x in data)) / len(data)
    return math.sqrt(variance)