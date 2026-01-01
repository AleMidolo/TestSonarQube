def mode(self, data):
    """
        Calcular la moda de un conjunto de datos
        :param data: list, lista de datos
        :return: float, la moda
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
    if not data:
        return []
    counter = Counter(data)
    max_count = max(counter.values())
    modes = [value for value, count in counter.items() if count == max_count]
    return sorted(modes)