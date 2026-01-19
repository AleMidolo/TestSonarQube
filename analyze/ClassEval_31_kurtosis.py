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
    if n < 4:
        raise ValueError('Data must have at least 4 elements to calculate kurtosis')
    mean = sum(data) / n
    variance = sum(((x - mean) ** 2 for x in data)) / n
    if variance == 0:
        return 0
    m4 = sum(((x - mean) ** 4 for x in data)) / n
    kurt = m4 / variance ** 2 - 3
    return kurt