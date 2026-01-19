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
    if not data:
        return None
    count = Counter(data)
    max_count = max(count.values())
    if max_count == 1:
        return list(set(data))
    modes = [item for item, freq in count.items() if freq == max_count]
    return sorted(modes)