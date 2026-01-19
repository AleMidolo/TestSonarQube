@staticmethod
def mean(data):
    """
    calcola la media della lista fornita.
    :param data: la lista fornita, lista.
    :return: la media della lista fornita, float.
    >>> statistics3 = Statistics3()
    >>> statistics3.mean([1, 2, 3])
    2.0

    """
    if not data:
        return 0.0
    return float(sum(data)) / len(data)