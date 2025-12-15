def correlation_coefficient(data1, data2):
    """
    Calculate the correlation coefficient of two sets of data.
    :param data1: The first set of data,list.
    :param data2: The second set of data,list.
    :return: The correlation coefficient, float.
    >>> correlation_coefficient([1, 2, 3], [4, 5, 6])
    0.9999999999999998

    """
    if len(data1) != len(data2):
        raise ValueError("Data sets must have the same length.")
    
    n = len(data1)
    mean1 = sum(data1) / n
    mean2 = sum(data2) / n
    
    numerator = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))
    denominator1 = math.sqrt(sum((data1[i] - mean1) ** 2 for i in range(n)))
    denominator2 = math.sqrt(sum((data2[i] - mean2) ** 2 for i in range(n)))
    
    if denominator1 == 0 or denominator2 == 0:
        return 0.0
    
    correlation = numerator / (denominator1 * denominator2)
    
    return correlation