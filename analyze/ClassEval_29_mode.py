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
    
    # Count frequency of each element
    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1
    
    # Find the maximum frequency
    max_freq = max(frequency.values())
    
    # Find all values with maximum frequency
    modes = [key for key, freq in frequency.items() if freq == max_freq]
    
    # Sort the modes for consistent output
    modes.sort()
    
    return modes