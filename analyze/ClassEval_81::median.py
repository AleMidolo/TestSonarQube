def median(data):
    """
    दी गई लिस्ट का मीडियन कैलकुलेट करता है।

    :param data: list, दी गई लिस्ट
    :return: float, दी गई लिस्ट का मीडियन

    >>> statistics3 = Statistics3()
    >>> statistics3.median([1, 2, 3, 4])
    2.5
    """
    
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
    else:
        return sorted_data[mid]