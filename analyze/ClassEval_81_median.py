def median(data):
    """
    calculates the median of the given list.
    :param data: the given list, list.
    :return: the median of the given list, float.
    >>> statistics3 = Statistics3()
    >>> statistics3.median([1, 2, 3, 4])
    2.5

    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n % 2 == 0:
        # Even number of elements: average of two middle elements
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        # Odd number of elements: middle element
        return float(sorted_data[n // 2])