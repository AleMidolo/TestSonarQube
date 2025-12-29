def get_correlation(self):
    """
        Calculate correlation
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation()
        1.0
        """
    if len(self.data) < 2:
        return 0.0
    x = self.data[:-1]
    y = self.data[1:]
    correlation = np.corrcoef(x, y)[0, 1]
    if np.isnan(correlation):
        return 1.0 if len(np.unique(self.data)) == 1 else 0.0
    return round(correlation, 2)