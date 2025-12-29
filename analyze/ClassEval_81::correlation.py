@staticmethod
def correlation(x, y):
    """
        计算给定列表的相关性。
        :param x: 给定列表，list。
        :param y: 给定列表，list。
        :return: 给定列表的相关性，float。
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation([1, 2, 3], [4, 5, 6])
        1.0

        """
    if len(x) != len(y):
        return None
    if len(x) < 2:
        return None
    mean_x = Statistics3.mean(x)
    mean_y = Statistics3.mean(y)
    std_x = Statistics3.standard_deviation(x)
    std_y = Statistics3.standard_deviation(y)
    if std_x is None or std_y is None or std_x == 0 or (std_y == 0):
        return None
    n = len(x)
    covariance = sum(((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))) / (n - 1)
    return covariance / (std_x * std_y)