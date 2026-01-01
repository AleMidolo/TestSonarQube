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
    if n < 4:
        return 0.0
    mean = sum(data) / n
    variance = sum(((x - mean) ** 2 for x in data)) / n
    if variance == 0:
        return 0.0
    m4 = sum(((x - mean) ** 4 for x in data)) / n
    kurt = m4 / variance ** 2 - 3
    return kurt