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
    frequency = {}
    for value in data:
        frequency[value] = frequency.get(value, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    return sorted(modes)