def get_min(self):
    """
    计算数据中的最小值
    :return: float
    >>> ds2 = DataStatistics2([1, 2, 3, 4])
    >>> ds2.get_min()
    1
    """
    return min(self.data)