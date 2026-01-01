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
    std_dev = math.sqrt(sum(((x - mean) ** 2 for x in data)) / n)
    if std_dev == 0:
        return math.nan
    centered_data = [x - mean for x in data]
    third_moment = sum((x ** 3 for x in centered_data)) / n
    skewness_value = third_moment / std_dev ** 3
    return skewness_value