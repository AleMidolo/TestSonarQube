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
    
    # 计算协方差的分子
    numerator = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))
    
    # 计算标准差的分母
    sum_sq1 = sum((x - mean1) ** 2 for x in data1)
    sum_sq2 = sum((x - mean2) ** 2 for x in data2)
    
    denominator = (sum_sq1 * sum_sq2) ** 0.5
    
    if denominator == 0:
        return 0
    
    return numerator / denominator