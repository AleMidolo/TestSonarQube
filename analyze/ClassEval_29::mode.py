def mode(self, data):
    """
        Calcola la moda di un insieme di dati
        :param data: list, lista dei dati
        :return: float, la moda
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
    count = Counter(data)
    max_count = max(count.values())
    modes = [key for key, value in count.items() if value == max_count]
    return modes