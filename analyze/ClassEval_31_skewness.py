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
    if n < 3:
        return math.nan
    mean = sum(data) / n
    variance = sum(((x - mean) ** 2 for x in data)) / n
    if variance == 0:
        return math.nan
    std_dev = math.sqrt(variance)
    skewness_value = sum(((x - mean) ** 3 for x in data)) / n / std_dev ** 3
    return skewness_value