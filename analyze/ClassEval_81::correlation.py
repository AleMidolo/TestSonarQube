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
    numerator = sum(((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)))
    denominator = math.sqrt(sum(((xi - mean_x) ** 2 for xi in x)) * sum(((yi - mean_y) ** 2 for yi in y)))
    if denominator == 0:
        return None
    return numerator / denominator