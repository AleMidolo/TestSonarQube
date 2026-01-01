def get_correlation(self):
    """
        सहसंबंध की गणना करें
        :return:float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation()
        1.0
        """
    if len(self.data) < 2:
        return float('nan')
    mean_x = np.mean(self.data)
    mean_y = np.mean(self.data)
    covariance = np.mean((self.data - mean_x) * (self.data - mean_y))
    std_x = np.std(self.data)
    std_y = np.std(self.data)
    if std_x == 0 or std_y == 0:
        return float('nan')
    correlation = covariance / (std_x * std_y)
    return round(correlation, 2)