@staticmethod
def skewness(data):
    """
    डेटा के एक सेट का स्क्यूनेस (skewness) निकालें।
    :param data: इनपुट डेटा सूची, सूची।
    :return: स्क्यूनेस, फ्लोट।
    >>> DataStatistics4.skewness([1, 2, 5])
    2.3760224064818463

    """
    n = len(data)
    mean = sum(data) / n
    
    # Calculate standard deviation
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = variance ** 0.5
    
    # Calculate skewness using the formula:
    # skewness = (n / ((n-1) * (n-2))) * sum((x - mean)^3) / std_dev^3
    if std_dev == 0:
        return 0.0
    
    m3 = sum((x - mean) ** 3 for x in data) / n
    skewness = m3 / (std_dev ** 3)
    
    # Apply sample correction factor
    if n > 2:
        skewness = skewness * ((n * (n - 1)) ** 0.5) / (n - 2)
    
    return skewness