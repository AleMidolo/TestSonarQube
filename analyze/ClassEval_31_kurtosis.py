@staticmethod
def kurtosis(data):
    """
    Calculate the kurtosis of a set of data.
    :param data: The input data list, list.
    :return: The kurtosis, float.
    >>> DataStatistics4.kurtosis([1, 20,100])
    -1.5000000000000007

    """
    n = len(data)
    if n < 2:
        return 0.0
    
    # Calculate mean
    mean = sum(data) / n
    
    # Calculate standard deviation
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = variance ** 0.5
    
    if std_dev == 0:
        return 0.0
    
    # Calculate fourth moment
    fourth_moment = sum((x - mean) ** 4 for x in data) / n
    
    # Calculate kurtosis (excess kurtosis)
    kurt = (fourth_moment / (variance ** 2)) - 3
    
    return kurt