@staticmethod
def standard_deviation(data):
    """
        calcola la deviazione standard della lista fornita.
        :param data: la lista fornita, lista.
        :return: la deviazione standard della lista fornita, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.standard_deviation([1, 2, 3])
        1.0

        """
    if len(data) == 0:
        return None
    mean_val = Statistics3.mean(data)
    if mean_val is None:
        return None
    variance = sum(((x - mean_val) ** 2 for x in data)) / len(data)
    return math.sqrt(variance)