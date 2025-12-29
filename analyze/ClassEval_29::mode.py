def mode(self, data):
    """
        Calculate the mode of a set of data
        :param data:list, data list
        :return:float, the mode
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
    if not data:
        return []
    counter = Counter(data)
    max_count = max(counter.values())
    modes = [item for item, count in counter.items() if count == max_count]
    return sorted(modes)