@staticmethod
def correlation_coefficient(data1, data2):
    """
        दो डेटा सेटों का सहसंबंध गुणांक निकालें।
        :param data1: पहला डेटा सेट, सूची।
        :param data2: दूसरा डेटा सेट, सूची।
        :return: सहसंबंध गुणांक, फ्लोट।
        >>> DataStatistics4.correlation_coefficient([1, 2, 3], [4, 5, 6])
        0.9999999999999998

        """
    if len(data1) != len(data2):
        raise ValueError('Both datasets must have the same length')
    n = len(data1)
    if n < 2:
        raise ValueError('Datasets must have at least 2 elements')
    mean1 = sum(data1) / n
    mean2 = sum(data2) / n
    numerator = sum(((data1[i] - mean1) * (data2[i] - mean2) for i in range(n)))
    denominator = math.sqrt(sum(((x - mean1) ** 2 for x in data1)) * sum(((y - mean2) ** 2 for y in data2)))
    if denominator == 0:
        return math.nan
    return numerator / denominator