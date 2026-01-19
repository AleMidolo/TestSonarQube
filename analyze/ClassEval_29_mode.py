def mode(self, data):
    """
    Calcola la moda di un insieme di dati
    :param data: list, lista dei dati
    :return: float, la moda
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
    
    # Find maximum frequency
    max_freq = max(frequency.values())
    
    # Get all values with maximum frequency
    modes = [key for key, freq in frequency.items() if freq == max_freq]
    
    # Sort the modes for consistent output
    modes.sort()
    
    return modes