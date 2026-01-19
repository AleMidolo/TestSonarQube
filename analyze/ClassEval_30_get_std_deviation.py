def get_std_deviation(self):
    """
    计算标准差，精确到小数点后两位
    :return: float
    >>> ds2 = DataStatistics2([1, 2, 3, 4])
    >>> ds2.get_std_deviation()
    1.12
    """
    if not self.data or len(self.data) == 0:
        return 0.0
    
    # 计算平均值
    mean = sum(self.data) / len(self.data)
    
    # 计算方差
    variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
    
    # 计算标准差
    std_dev = variance ** 0.5
    
    # 精确到小数点后两位
    return round(std_dev, 2)