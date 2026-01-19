@staticmethod
def correlation_coefficient(data1, data2):
    """
        Calcular el coeficiente de correlación de dos conjuntos de datos.
        :param data1: El primer conjunto de datos, lista.
        :param data2: El segundo conjunto de datos, lista.
        :return: El coeficiente de correlación, float.
        >>> DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6])
        0.9999999999999998

        """
    if len(data1) != len(data2):
        raise ValueError('Las listas de datos deben tener la misma longitud')
    n = len(data1)
    mean1 = sum(data1) / n
    mean2 = sum(data2) / n
    numerator = sum(((data1[i] - mean1) * (data2[i] - mean2) for i in range(n)))
    sum_sq1 = sum(((x - mean1) ** 2 for x in data1))
    sum_sq2 = sum(((x - mean2) ** 2 for x in data2))
    denominator = math.sqrt(sum_sq1 * sum_sq2)
    if denominator == 0:
        return math.nan
    return numerator / denominator