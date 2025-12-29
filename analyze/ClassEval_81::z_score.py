@staticmethod
def z_score(data):
    """
        计算给定列表的 z-score。
        :param data: 给定的列表，list。
        :return: 给定列表的 z-score，list。
        >>> statistics3 = Statistics3()
        >>> statistics3.z_score([1, 2, 3, 4])
        [-1.161895003862225, -0.3872983346207417, 0.3872983346207417, 1.161895003862225]

        """
    mean_value = Statistics3.mean(data)
    std_dev = Statistics3.standard_deviation(data)
    if std_dev is None:
        return None
    return [(x - mean_value) / std_dev for x in data]