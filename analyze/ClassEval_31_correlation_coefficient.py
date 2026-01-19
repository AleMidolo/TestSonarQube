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
    
    # Calculate numerator: sum of (x - mean_x) * (y - mean_y)
    numerator = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))
    
    # Calculate denominator: sqrt(sum of (x - mean_x)^2) * sqrt(sum of (y - mean_y)^2)
    sum_sq1 = sum((data1[i] - mean1) ** 2 for i in range(n))
    sum_sq2 = sum((data2[i] - mean2) ** 2 for i in range(n))
    denominator = (sum_sq1 ** 0.5) * (sum_sq2 ** 0.5)
    
    # Calculate correlation coefficient
    return numerator / denominator