def get_correlation(self):
    """
        Calcular la correlación
        :return: float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation()
        1.0
        """
    if len(self.data) < 2:
        return 1.0
    data_copy = self.data.copy()
    correlation_matrix = np.corrcoef(self.data, data_copy)
    correlation = correlation_matrix[0, 0]
    return round(correlation, 2)