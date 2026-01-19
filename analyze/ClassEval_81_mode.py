@staticmethod
def mode(data):
    """
        calcula la moda de la lista dada.
        :param data: la lista dada, lista.
        :return: la moda de la lista dada, lista.
        >>> statistics3 = Statistics3()
        >>> statistics3.mode([1, 2, 3, 3])
        [3]

        """
    from collections import Counter
    if not data:
        return []
    count = Counter(data)
    max_count = max(count.values())
    return [num for num, freq in count.items() if freq == max_count]