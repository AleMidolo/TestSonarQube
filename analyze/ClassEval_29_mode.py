def mode(self, data):
    """
    计算一组数据的众数
    :param data:list, 数据列表
    :return:float, 众数
    >>> ds = DataStatistics()
    >>> ds.mode([2, 2, 3, 3, 4])
    [2, 3]
    """
    if not data:
        return []
    
    # 统计每个元素出现的频率
    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1
    
    # 找到最大频率
    max_frequency = max(frequency.values())
    
    # 找到所有具有最大频率的值
    modes = [key for key, freq in frequency.items() if freq == max_frequency]
    
    # 排序后返回
    return sorted(modes)