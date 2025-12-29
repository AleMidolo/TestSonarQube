def get_correlation(self):
    """
        सहसंबंध की गणना करें
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation()
        1.0
        """
    if len(self.data) < 2:
        return 1.0
    corr_matrix = np.corrcoef(self.data, self.data)
    return round(corr_matrix[0, 1], 2)