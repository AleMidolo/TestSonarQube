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
    if max_count == 1:
        return list(set(data))
    modes = [item for item, freq in count.items() if freq == max_count]
    return sorted(modes)