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
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1
    
    max_frequency = max(frequency.values())
    
    modes = [key for key, freq in frequency.items() if freq == max_frequency]
    
    return modes