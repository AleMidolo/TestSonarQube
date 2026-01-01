@staticmethod
def standard_deviation(data):
    """
        calculates the standard deviation of the given list.
        :param data: the given list, list.
        :return: the standard deviation of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.standard_deviation([1, 2, 3])
        1.0

        """
    if len(data) == 0:
        return None
    mean = Statistics3.mean(data)
    variance = sum(((x - mean) ** 2 for x in data)) / len(data)
    return math.sqrt(variance)