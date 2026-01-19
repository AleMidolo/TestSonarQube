@staticmethod
def mode(data):
    """
    calculates the mode of the given list.
    :param data: the given list, list.
    :return: the mode of the given list, list.
    >>> statistics3 = Statistics3()
    >>> statistics3.mode([1, 2, 3, 3])
    [3]

    """
    if not data:
        return []
    
    frequency = {}
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1
    
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    
    return modes