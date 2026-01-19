@staticmethod
def kurtosis(data):
    """
    डेटा के एक सेट का कर्टोसिस निकालें।
    :param data: इनपुट डेटा सूची, सूची।
    :return: कर्टोसिस, फ्लोट।
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
    
    # Calculate kurtosis (excess kurtosis)
    fourth_moment = sum((x - mean) ** 4 for x in data) / n
    kurtosis_value = (fourth_moment / (variance ** 2)) - 3
    
    return kurtosis_value