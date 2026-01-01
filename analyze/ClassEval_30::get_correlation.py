def get_correlation(self):
    """
        सहसंबंध की गणना करें
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation()
        1.0
        """
    correlation_matrix = np.corrcoef(self.data, self.data)
    return round(correlation_matrix[0, 1], 2)