@staticmethod
def mode(data):
    """
        calculates the mode of the given list.
        :param data: the given list, list.
        :return: the mode of the given list, list.
        >>> statistics3 = Statistics3()
        >>> statistics3.mode([1, 2, 3, 3])
        [3]

        """
    from collections import Counter
    count = Counter(data)
    max_count = max(count.values())
    return [x for x, freq in count.items() if freq == max_count]