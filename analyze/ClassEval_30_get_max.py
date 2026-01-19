def get_max(self):
    """
    Calcola il valore massimo nei dati
    :return: float
    >>> ds2 = DataStatistics2([1, 2, 3, 4])
    >>> ds2.get_max()
    4
    """
    return max(self.data)