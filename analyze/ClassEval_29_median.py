def median(self, data):
    """
        计算一组数据的中位数，精确到小数点后两位
        :param data:list, 数据列表
        :return:float, 中位数值
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 1:
        median_value = sorted_data[n // 2]
    else:
        median_value = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    return round(median_value, 2)