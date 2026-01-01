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
    if n % 2 == 1:
        median_value = sorted_data[n // 2]
    else:
        median_value = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    return round(median_value, 2)