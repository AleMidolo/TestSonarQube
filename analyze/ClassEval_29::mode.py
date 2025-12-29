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
    counter = Counter(data)
    max_count = max(counter.values())
    modes = [key for key, count in counter.items() if count == max_count]
    return sorted(modes)