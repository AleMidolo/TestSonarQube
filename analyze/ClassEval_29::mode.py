def mode(self, data):
    """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
    count = Counter(data)
    max_count = max(count.values())
    return [key for key, value in count.items() if value == max_count]