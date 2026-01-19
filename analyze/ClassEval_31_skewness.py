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
    mean = sum(data) / n
    
    # Calculate standard deviation
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = variance ** 0.5
    
    # Calculate skewness using the formula
    # skewness = (n / ((n-1) * (n-2))) * sum((x - mean)^3) / std_dev^3
    if std_dev == 0:
        return 0.0
    
    sum_cubed_deviations = sum((x - mean) ** 3 for x in data)
    skewness = (n / ((n - 1) * (n - 2))) * sum_cubed_deviations / (std_dev ** 3)
    
    return skewness