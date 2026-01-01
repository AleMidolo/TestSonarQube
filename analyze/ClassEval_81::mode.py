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
    if not data:
        return None
    count_dict = Counter(data)
    max_count = max(count_dict.values())
    modes = [item for item, count in count_dict.items() if count == max_count]
    return sorted(modes)