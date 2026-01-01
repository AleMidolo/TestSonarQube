@staticmethod
def skewness(data):
    """
        Calcola la asimmetria di un insieme di dati.
        :param data: La lista di dati in ingresso, list.
        :return: L'asimmetria, float.
        >>> DataStatistics4.skewness([1, 2, 5])
        2.3760224064818463

        """
    n = len(data)
    if n < 2:
        return math.nan
    mean = sum(data) / n
    variance = sum(((x - mean) ** 2 for x in data)) / n
    if variance == 0:
        return math.nan
    std_dev = math.sqrt(variance)
    third_moment = sum(((x - mean) ** 3 for x in data)) / n
    skewness_value = third_moment / std_dev ** 3
    return skewness_value