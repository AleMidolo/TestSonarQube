def get_correlation(self):
    """
    सहसंबंध की गणना करें
    :return:float
    >>> ds2 = DataStatistics2([1, 2, 3, 4])
    >>> ds2.get_correlation()
    1.0
    """
    if len(self) < 2:
        return 1.0
    
    # Calculate correlation between indices and values
    n = len(self)
    indices = list(range(n))
    values = list(self)
    
    # Calculate means
    mean_x = sum(indices) / n
    mean_y = sum(values) / n
    
    # Calculate correlation coefficient
    numerator = sum((indices[i] - mean_x) * (values[i] - mean_y) for i in range(n))
    
    sum_sq_x = sum((indices[i] - mean_x) ** 2 for i in range(n))
    sum_sq_y = sum((values[i] - mean_y) ** 2 for i in range(n))
    
    denominator = (sum_sq_x * sum_sq_y) ** 0.5
    
    if denominator == 0:
        return 1.0
    
    return numerator / denominator