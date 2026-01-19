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
    
    # Count occurrences of each element
    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1
    
    # Find the maximum frequency
    max_frequency = max(frequency.values())
    
    # Find all values with the maximum frequency
    modes = [key for key, freq in frequency.items() if freq == max_frequency]
    
    return modes