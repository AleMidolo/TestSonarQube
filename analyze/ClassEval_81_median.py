def median(data):
    """
    计算给定列表的中位数。
    :param data: 给定的列表，list。
    :return: 给定列表的中位数，float。
    >>> statistics3 = Statistics3()
    >>> statistics3.median([1, 2, 3, 4])
    2.5

    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n % 2 == 0:
        # 偶数个元素，取中间两个数的平均值
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        # 奇数个元素，取中间的数
        return float(sorted_data[n // 2])