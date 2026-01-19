@staticmethod
def mean(data):
    """
        计算给定列表的平均值。
        :param data: 给定的列表，list。
        :return: 给定列表的平均值，float。
        >>> statistics3 = Statistics3()
        >>> statistics3.mean([1, 2, 3])
        2.0

        """
    return sum(data) / len(data)