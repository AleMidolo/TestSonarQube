def mode(self, data):
    """
        Calcular la moda de un conjunto de datos
        :param data: list, lista de datos
        :return: float, la moda
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
    count = Counter(data)
    max_count = max(count.values())
    modes = [key for key, value in count.items() if value == max_count]
    return modes