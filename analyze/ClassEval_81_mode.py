@staticmethod
def mode(data):
    """
    计算给定列表的众数。
    :param data: 给定的列表，list。
    :return: 给定列表的众数，list。
    >>> statistics3 = Statistics3()
    >>> statistics3.mode([1, 2, 3, 3])
    [3]

    """
    if not data:
        return []
    
    # Count frequency of each element
    frequency = {}
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1
    
    # Find the maximum frequency
    max_freq = max(frequency.values())
    
    # Find all elements with maximum frequency
    modes = [key for key, value in frequency.items() if value == max_freq]
    
    return modes