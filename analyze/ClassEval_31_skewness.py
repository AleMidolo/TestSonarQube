@staticmethod
def skewness(data):
    """
    计算一组数据的偏度。
    :param data: 输入数据列表，list。
    :return: 偏度，float。
    >>> DataStatistics4.skewness([1, 2, 5])
    2.3760224064818463

    """
    n = len(data)
    if n < 3:
        return 0.0
    
    # Calculate mean
    mean = sum(data) / n
    
    # Calculate standard deviation
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = variance ** 0.5
    
    if std_dev == 0:
        return 0.0
    
    # Calculate skewness using the formula:
    # skewness = (1/n) * Σ((x - mean) / std_dev)^3
    skew = sum(((x - mean) / std_dev) ** 3 for x in data) / n
    
    return skew