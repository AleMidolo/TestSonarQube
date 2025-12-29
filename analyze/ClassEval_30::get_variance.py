def get_variance(self):
    """
        Calcola la varianza, con una precisione di due cifre  decimali
        :return: float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_variance()
        1.25
        """
    return round(np.var(self.data), 2)