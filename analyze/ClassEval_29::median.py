def median(self, data):
    """
        Calcola la mediana di un gruppo di dati, con una precisione di due cifre decimali.
        :param data: list, lista dei dati
        :return: float, il valore della mediana
        >>> ds = DataStatistics()
        >>> ds.median([2, 5, 1, 3, 4])
        3.00
        """
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return round((sorted_data[mid - 1] + sorted_data[mid]) / 2, 2)
    else:
        return round(sorted_data[mid], 2)