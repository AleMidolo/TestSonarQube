@staticmethod
def correlation(x, y):
    """
        calculates the correlation of the given list.
        :param x: the given list, list.
        :param y: the given list, list.
        :return: the correlation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.correlation([1, 2, 3], [4, 5, 6])
        1.0
        """
    if len(x) != len(y):
        raise ValueError('Lists must be of the same length.')
    mean_x = Statistics3.mean(x)
    mean_y = Statistics3.mean(y)
    covariance = sum(((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x))))
    std_x = Statistics3.standard_deviation(x)
    std_y = Statistics3.standard_deviation(y)
    if std_x == 0 or std_y == 0:
        return None
    return covariance / ((len(x) - 1) * std_x * std_y)