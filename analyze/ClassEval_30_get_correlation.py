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
    data_shifted = np.roll(self.data, 1)
    if len(self.data) > 1:
        data_shifted[0] = self.data[1]
    correlation = np.corrcoef(self.data, data_shifted)[0, 1]
    if np.isnan(correlation):
        return 0.0
    return round(correlation, 2)