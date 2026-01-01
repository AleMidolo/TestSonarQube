def get_sum(self):
    """
        Calcola la somma dei dati
        :return: float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_sum()
        10
        """
    return np.sum(self.data)