@staticmethod
def mean(data):
    """
    calcula la media de la lista dada.
    :param data: la lista dada, lista.
    :return: la media de la lista dada, float.
    >>> statistics3 = Statistics3()
    >>> statistics3.mean([1, 2, 3])
    2.0

    """
    return sum(data) / len(data)