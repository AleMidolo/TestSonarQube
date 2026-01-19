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
    mean = sum(data) / n
    
    # Calculate the standard deviation
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = variance ** 0.5
    
    # Calculate skewness using the formula: E[((X - μ) / σ)^3]
    skewness = sum(((x - mean) / std_dev) ** 3 for x in data) / n
    
    return skewness