@staticmethod
def mode(data):
    """
    calcola la moda della lista fornita.
    :param data: la lista fornita, lista.
    :return: la moda della lista fornita, lista.
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
    
    # Find maximum frequency
    max_freq = max(frequency.values())
    
    # Find all elements with maximum frequency
    modes = [key for key, value in frequency.items() if value == max_freq]
    
    return modes