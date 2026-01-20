@staticmethod
def z_score(data):
    """
    calcula el z-score de la lista dada.
    :param data: la lista dada, lista.
    :return: el z-score de la lista dada, lista.
    >>> statistics3 = Statistics3()
    >>> statistics3.z_score([1, 2, 3, 4])
    [-1.161895003862225, -0.3872983346207417, 0.3872983346207417, 1.161895003862225]

    """
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    return [(x - mean) / std_dev for x in data]