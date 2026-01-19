def correlation_coefficient(data1, data2):
    """
    计算两组数据的相关系数。
    :param data1: 第一组数据，列表。
    :param data2: 第二组数据，列表。
    :return: 相关系数，浮点数。
    >>> DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6])
    0.9999999999999998

    """
    if len(data1) != len(data2) or len(data1) == 0:
        return 0
    
    n = len(data1)
    
    # 计算均值
    mean1 = sum(data1) / n
    mean2 = sum(data2) / n
    
    # 计算协方差和标准差
    covariance = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))
    
    # 计算标准差
    std1 = (sum((x - mean1) ** 2 for x in data1)) ** 0.5
    std2 = (sum((x - mean2) ** 2 for x in data2)) ** 0.5
    
    # 避免除以零
    if std1 == 0 or std2 == 0:
        return 0
    
    # 计算相关系数
    correlation = covariance / (std1 * std2)
    
    return correlation