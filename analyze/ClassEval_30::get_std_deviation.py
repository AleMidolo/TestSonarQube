def get_std_deviation(self):
    """
        Calcola la deviazione standard, con una precisione di due cifre  decimali
        :return: float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_std_deviation()
        1.12
        """
    return round(np.std(self.data), 2)