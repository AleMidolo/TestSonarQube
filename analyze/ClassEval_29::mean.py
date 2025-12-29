def mean(self, data):
    """
        Calcola il valore medio di un gruppo di dati, con una precisione di due cifre decimali.
        :param data: list, lista dei dati
        :return: float, il valore medio
        >>> ds = DataStatistics()
        >>> ds.mean([1, 2, 3, 4, 5])
        3.00
        """
    return round(sum(data) / len(data), 2)