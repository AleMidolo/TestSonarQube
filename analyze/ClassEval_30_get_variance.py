def get_variance(self):
    """
    计算方差，精确到小数点后两位
    :return: float
    >>> ds2 = DataStatistics2([1, 2, 3, 4])
    >>> ds2.get_variance()
    1.25
    """
    if not self.data or len(self.data) == 0:
        return 0.0
    
    # 计算平均值
    mean = sum(self.data) / len(self.data)
    
    # 计算方差：每个数据点与平均值差的平方和除以数据点个数
    variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
    
    # 精确到小数点后两位
    return round(variance, 2)