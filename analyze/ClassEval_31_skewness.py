@staticmethod
def skewness(data):
    """
    Calculate the skewness of a set of data.
    :param data: The input data list, list.
    :return: The skewness, float.
    >>> DataStatistics4.skewness([1, 2, 5])
    2.3760224064818463

    """
    n = len(data)
    mean = sum(data) / n
    
    # Calculate the standard deviation
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = variance ** 0.5
    
    # Calculate skewness using the formula:
    # skewness = (n / ((n-1) * (n-2))) * sum((x - mean)^3) / std_dev^3
    if std_dev == 0:
        return 0.0
    
    # Calculate the third moment
    third_moment = sum((x - mean) ** 3 for x in data)
    
    # Apply the sample skewness formula
    skewness = (n / ((n - 1) * (n - 2))) * (third_moment / (std_dev ** 3))
    
    return skewness