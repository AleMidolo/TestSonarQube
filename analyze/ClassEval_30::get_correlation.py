def get_correlation(self):
    """
        Calcola la correlazione
        :return: float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation()
        1.0
        """
    if len(self.data) < 2:
        return 0.0
    x = np.arange(len(self.data))
    y = self.data
    correlation = np.corrcoef(x, y)[0, 1]
    if np.isnan(correlation):
        return 0.0
    return round(correlation, 2)