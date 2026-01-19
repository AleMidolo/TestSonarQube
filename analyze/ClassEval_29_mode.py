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
    max_freq = max(count.values())
    modes = [key for key, freq in count.items() if freq == max_freq]
    return modes