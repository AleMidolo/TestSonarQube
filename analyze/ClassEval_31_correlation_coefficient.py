@staticmethod
def correlation_coefficient(data1, data2):
    """
        Calcola il coefficiente di correlazione di due insiemi di dati.
        :param data1: Il primo insieme di dati, lista.
        :param data2: Il secondo insieme di dati, lista.
        :return: Il coefficiente di correlazione, float.
        >>> DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6])
        0.9999999999999998

        """
    if len(data1) != len(data2):
        raise ValueError('Le due liste devono avere la stessa lunghezza')
    n = len(data1)
    if n < 2:
        raise ValueError('Le liste devono contenere almeno 2 elementi')
    mean1 = sum(data1) / n
    mean2 = sum(data2) / n
    numerator = sum(((data1[i] - mean1) * (data2[i] - mean2) for i in range(n)))
    denominator = math.sqrt(sum(((x - mean1) ** 2 for x in data1)) * sum(((y - mean2) ** 2 for y in data2)))
    if denominator == 0:
        return math.nan
    return numerator / denominator