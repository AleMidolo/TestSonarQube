@staticmethod
def kurtosis(data):
    """
    计算一组数据的峰度。
    :param data: 输入数据列表，list。
    :return: 峰度，float。
    >>> DataStatistics4.kurtosis([1, 20,100])
    -1.5000000000000007

    """
    n = len(data)
    if n < 2:
        return 0.0
    
    # 计算均值
    mean = sum(data) / n
    
    # 计算标准差
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = variance ** 0.5
    
    if std_dev == 0:
        return 0.0
    
    # 计算四阶中心矩
    fourth_moment = sum((x - mean) ** 4 for x in data) / n
    
    # 计算峰度（超值峰度，excess kurtosis）
    kurtosis_value = fourth_moment / (variance ** 2) - 3
    
    return kurtosis_value