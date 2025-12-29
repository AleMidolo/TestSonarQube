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
    n = len(x)
    if n < 2:
        return None
    mean_x = Statistics3.mean(x)
    mean_y = Statistics3.mean(y)
    numerator = sum(((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)))
    denominator_x = sum(((xi - mean_x) ** 2 for xi in x))
    denominator_y = sum(((yi - mean_y) ** 2 for yi in y))
    if denominator_x == 0 or denominator_y == 0:
        return None
    return numerator / math.sqrt(denominator_x * denominator_y)