@staticmethod
def standard_deviation(data):
    """
    calcola la deviazione standard della lista fornita.
    :param data: la lista fornita, lista.
    :return: la deviazione standard della lista fornita, float.
    >>> statistics3 = Statistics3()
    >>> statistics3.standard_deviation([1, 2, 3])
    1.0

    """
    if not data:
        return 0.0
    
    # Calculate mean
    mean = sum(data) / len(data)
    
    # Calculate variance (sum of squared differences from mean)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    
    # Standard deviation is square root of variance
    return variance ** 0.5