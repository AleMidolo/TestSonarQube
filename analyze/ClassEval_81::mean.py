@staticmethod
def mean(data):
    """
        calculates the mean of the given list.
        :param data: the given list, list.
        :return: the mean of the given list, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.mean([1, 2, 3])
        2.0

        """
    if not data:
        return None
    return sum(data) / len(data)