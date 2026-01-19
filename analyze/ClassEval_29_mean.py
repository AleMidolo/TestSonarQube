def mean(self, data):
    """
    计算一组数据的平均值，精确到小数点后两位
    :param data:list, 数据列表
    :return:float, 平均值
    >>> ds = DataStatistics()
    >>> ds.mean([1, 2, 3, 4, 5])
    3.00
    """
    if not data:
        return 0.00
    
    total = sum(data)
    average = total / len(data)
    return round(average, 2)