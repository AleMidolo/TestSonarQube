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
    n = len(x)
    if n < 2:
        return None
    mean_x = Statistics3.mean(x)
    mean_y = Statistics3.mean(y)
    numerator = sum(((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)))
    denominator = math.sqrt(sum(((x[i] - mean_x) ** 2 for i in range(n))) * sum(((y[i] - mean_y) ** 2 for i in range(n))))
    if denominator == 0:
        return None
    return numerator / denominator