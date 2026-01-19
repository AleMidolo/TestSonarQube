def correlation_coefficient(data1, data2):
    """
    Calculate the correlation coefficient of two sets of data.
    :param data1: The first set of data,list.
    :param data2: The second set of data,list.
    :return: The correlation coefficient, float.
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
    
    # Calculate correlation coefficient
    return numerator / denominator