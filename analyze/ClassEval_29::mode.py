def mode(self, data):
    """
        计算一组数据的众数
        :param data:list, 数据列表
        :return:float, 众数
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
    count = Counter(data)
    max_freq = max(count.values())
    modes = [key for key, freq in count.items() if freq == max_freq]
    return modes