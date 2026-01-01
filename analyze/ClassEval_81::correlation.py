@staticmethod
def correlation(x, y):
    """
        calcola la correlazione della lista fornita.
        :param x: la lista fornita, lista.
        :param y: la lista fornita, lista.
        :return: la correlazione della lista fornita, float.
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