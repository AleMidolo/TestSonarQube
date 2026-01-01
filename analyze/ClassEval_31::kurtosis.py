@staticmethod
def kurtosis(data):
    """
        Calcular la curtosis de un conjunto de datos.
        :param data: La lista de datos de entrada, lista.
        :return: La curtosis, float.
        >>> DataStatistics4.kurtosis([1, 20, 100])
        -1.5000000000000007
        """
    n = len(data)
    mean = sum(data) / n
    variance = sum(((x - mean) ** 2 for x in data)) / n
    std_deviation = math.sqrt(variance)
    kurtosis = sum(((x - mean) ** 4 for x in data)) * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * std_deviation ** 4) - 3 * (n - 1) ** 2 / ((n - 2) * (n - 3)) if std_deviation != 0 else 0
    return kurtosis