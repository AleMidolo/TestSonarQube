def get_correlation(self):
    """
        सहसंबंध की गणना करें
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation()
        1.0
        """
    if len(self.data) < 2:
        return 0.0
    indices = np.arange(len(self.data))
    correlation_matrix = np.corrcoef(self.data, indices)
    correlation = correlation_matrix[0, 1]
    return round(correlation, 2)