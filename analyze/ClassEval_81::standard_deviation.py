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
    mean_value = Statistics3.mean(data)
    if mean_value is None:
        return None
    variance = sum(((x - mean_value) ** 2 for x in data)) / len(data)
    return math.sqrt(variance)