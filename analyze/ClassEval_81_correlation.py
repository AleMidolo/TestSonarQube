@staticmethod
def correlation(x, y):
    """
        calcula la correlación de la lista dada.
        :param x: la lista dada, lista.
        :param y: la lista dada, lista.
        :return: la correlación de la lista dada, float.
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
    numerator = sum(((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)))
    denominator = (n - 1) * std_x * std_y
    return numerator / denominator