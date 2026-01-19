def correlation_coefficient(data1, data2):
    """
    Calcola il coefficiente di correlazione di due insiemi di dati.
    :param data1: Il primo insieme di dati, lista.
    :param data2: Il secondo insieme di dati, lista.
    :return: Il coefficiente di correlazione, float.
    >>> DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6])
    0.9999999999999998

    """
    n = len(data1)
    
    # Calculate means
    mean1 = sum(data1) / n
    mean2 = sum(data2) / n
    
    # Calculate numerator (covariance)
    numerator = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))
    
    # Calculate denominator (product of standard deviations)
    sum_sq1 = sum((x - mean1) ** 2 for x in data1)
    sum_sq2 = sum((x - mean2) ** 2 for x in data2)
    denominator = (sum_sq1 * sum_sq2) ** 0.5
    
    # Return correlation coefficient
    return numerator / denominator