@staticmethod
def kurtosis(data):
    """
    Calcola la curtosi di un insieme di dati.
    :param data: La lista di dati in input, list.
    :return: La curtosi, float.
    >>> DataStatistics4.kurtosis([1, 20,100])
    -1.5000000000000007

    """
    n = len(data)
    if n < 4:
        raise ValueError("Kurtosis requires at least 4 data points")
    
    # Calculate mean
    mean = sum(data) / n
    
    # Calculate standard deviation
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = variance ** 0.5
    
    if std_dev == 0:
        raise ValueError("Standard deviation is zero")
    
    # Calculate kurtosis (excess kurtosis)
    fourth_moment = sum((x - mean) ** 4 for x in data) / n
    kurtosis_value = (fourth_moment / (variance ** 2)) - 3
    
    return kurtosis_value