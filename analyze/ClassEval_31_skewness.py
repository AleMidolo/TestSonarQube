@staticmethod
def skewness(data):
    """
        Calcular la asimetría de un conjunto de datos.
        :param data: La lista de datos de entrada, lista.
        :return: La asimetría, float.
        >>> DataStatistics4.skewness([1, 2, 5])
        2.3760224064818463

        """
    n = len(data)
    if n < 3:
        return math.nan
    mean = sum(data) / n
    variance = sum(((x - mean) ** 2 for x in data)) / n
    if variance == 0:
        return math.nan
    std_dev = math.sqrt(variance)
    third_moment = sum((((x - mean) / std_dev) ** 3 for x in data)) / n
    if n > 3:
        correction = math.sqrt(n * (n - 1)) / (n - 2)
        return third_moment * correction
    else:
        return third_moment