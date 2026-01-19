@staticmethod
def median(data):
    """
        calcola la mediana della lista fornita.
        :param data: la lista fornita, lista.
        :return: la mediana della lista fornita, float.
        >>> statistics3 = Statistics3()
        >>> statistics3.median([1, 2, 3, 4])
        2.5

        """
    if len(data) == 0:
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]