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
    data2 = self.data.copy()
    correlation_matrix = np.corrcoef(self.data, data2)
    correlation = correlation_matrix[0, 1]
    return round(correlation, 2)