def get_correlation(self):
    """
        Calculate correlation
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation()
        1.0
        """
    return np.corrcoef(self.data, self.data)[0, 1]