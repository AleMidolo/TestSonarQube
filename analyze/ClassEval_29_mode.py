def mode(self, data):
    """
        Calcola la moda di un insieme di dati
        :param data: list, lista dei dati
        :return: float, la moda
        >>> ds = DataStatistics()
        >>> ds.mode([2, 2, 3, 3, 4])
        [2, 3]
        """
    if not data:
        return []
    counter = Counter(data)
    max_count = max(counter.values())
    modes = [key for key, count in counter.items() if count == max_count]
    return sorted(modes)