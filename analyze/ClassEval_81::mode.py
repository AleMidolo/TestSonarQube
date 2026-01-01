@staticmethod
def mode(data):
    """
        calcola la moda della lista fornita.
        :param data: la lista fornita, lista.
        :return: la moda della lista fornita, lista.
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