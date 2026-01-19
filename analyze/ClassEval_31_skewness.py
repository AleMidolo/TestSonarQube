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
    mean = sum(data) / n
    
    # Calculate standard deviation
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = variance ** 0.5
    
    # Calculate skewness
    skew = sum((x - mean) ** 3 for x in data) / n
    skew = skew / (std_dev ** 3)
    
    return skew