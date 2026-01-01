def get_correlation(self):
    """
        Calcular la correlación
        :return: float
        >>> ds2 = DataStatistics2([1, 2, 3, 4])
        >>> ds2.get_correlation()
        1.0
        """
    if len(self.data) < 2:
        return 0.0
    x = self.data[:-1]
    y = self.data[1:]
    correlation_matrix = np.corrcoef(x, y)
    correlation = correlation_matrix[0, 1]
    return round(correlation, 2)