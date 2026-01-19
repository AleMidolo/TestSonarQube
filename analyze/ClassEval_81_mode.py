@staticmethod
def mode(data):
    """
    दी गई लिस्ट का मोड कैलकुलेट करता है।

    :param data: list, दी गई लिस्ट
    :return: list, दी गई लिस्ट का मोड

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
    mode_list = [key for key, value in frequency.items() if value == max_freq]
    
    return mode_list