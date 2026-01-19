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
    if not data:
        return None
    count = Counter(data)
    max_count = max(count.values())
    modes = [value for value, freq in count.items() if freq == max_count]
    return sorted(modes)