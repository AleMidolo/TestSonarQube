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
    n = len(x)
    if n < 2:
        return None
    mean_x = Statistics3.mean(x)
    mean_y = Statistics3.mean(y)
    numerator = sum(((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)))
    denominator = math.sqrt(sum(((xi - mean_x) ** 2 for xi in x)) * sum(((yi - mean_y) ** 2 for yi in y)))
    if denominator == 0:
        return None
    return numerator / denominator