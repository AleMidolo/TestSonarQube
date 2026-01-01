@staticmethod
def correlation_coefficient(data1, data2):
    """
        计算两组数据的相关系数。
        :param data1: 第一组数据，列表。
        :param data2: 第二组数据，列表。
        :return: 相关系数，浮点数。
        >>> DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6])
        0.9999999999999998

        """
    n = len(data1)
    if n != len(data2) or n < 2:
        raise ValueError('两组数据长度必须相同且至少包含2个元素')
    mean1 = sum(data1) / n
    mean2 = sum(data2) / n
    numerator = sum(((data1[i] - mean1) * (data2[i] - mean2) for i in range(n)))
    denominator = math.sqrt(sum(((x - mean1) ** 2 for x in data1)) * sum(((y - mean2) ** 2 for y in data2)))
    if denominator == 0:
        return math.nan
    return numerator / denominator