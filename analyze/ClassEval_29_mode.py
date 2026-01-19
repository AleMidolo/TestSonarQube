def mode(self, data):
    """
    डेटा के एक सेट का मोड कैलकुलेट करें।

    :param data: list, डेटा लिस्ट
    :return: float, मोड

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
    max_frequency = max(frequency.values())
    
    # Find all values with maximum frequency
    modes = [key for key, freq in frequency.items() if freq == max_frequency]
    
    # Sort the modes for consistent output
    modes.sort()
    
    return modes