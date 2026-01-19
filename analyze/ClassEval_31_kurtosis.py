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
    mean = sum(data) / n
    variance = sum(((x - mean) ** 2 for x in data)) / n
    std_deviation = math.sqrt(variance)
    if std_deviation == 0:
        return 0
    kurtosis = sum(((x - mean) ** 4 for x in data)) * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3) * std_deviation ** 4) - 3 * (n - 1) ** 2 / ((n - 2) * (n - 3))
    return kurtosis