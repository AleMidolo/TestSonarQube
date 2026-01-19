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
    indices = np.arange(len(self.data))
    correlation_matrix = np.corrcoef(indices, self.data)
    return round(correlation_matrix[0, 1], 2)