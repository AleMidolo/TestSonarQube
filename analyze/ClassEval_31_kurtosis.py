@staticmethod
def kurtosis(data):
    """
        Calculate the kurtosis of a set of data.
        :param data: The input data list, list.
        :return: The kurtosis, float.
        >>> DataStatistics4.kurtosis([1, 20, 100])
        -1.5000000000000007
        """
    n = len(data)
    mean = sum(data) / n
    variance = sum(((x - mean) ** 2 for x in data)) / n
    if variance == 0:
        return 0
    m4 = sum(((x - mean) ** 4 for x in data)) / n
    kurt = m4 / variance ** 2 - 3
    return kurt