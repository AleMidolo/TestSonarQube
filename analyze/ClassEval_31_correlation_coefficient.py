def correlation_coefficient(data1, data2):
    """
    दो डेटा सेटों का सहसंबंध गुणांक निकालें।
    :param data1: पहला डेटा सेट, सूची।
    :param data2: दूसरा डेटा सेट, सूची।
    :return: सहसंबंध गुणांक, फ्लोट।
    >>> DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6])
    0.9999999999999998
    """
    n = len(data1)
    
    # Calculate means
    mean1 = sum(data1) / n
    mean2 = sum(data2) / n
    
    # Calculate numerator: sum of (xi - mean1) * (yi - mean2)
    numerator = sum((data1[i] - mean1) * (data2[i] - mean2) for i in range(n))
    
    # Calculate denominator: sqrt(sum of (xi - mean1)^2) * sqrt(sum of (yi - mean2)^2)
    sum_sq1 = sum((x - mean1) ** 2 for x in data1)
    sum_sq2 = sum((y - mean2) ** 2 for y in data2)
    denominator = (sum_sq1 ** 0.5) * (sum_sq2 ** 0.5)
    
    # Calculate correlation coefficient
    if denominator == 0:
        return 0.0
    
    return numerator / denominator